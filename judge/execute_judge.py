import os
import re
import shutil
import subprocess
import uuid

from django.conf import settings
from django.utils import timezone

from judge.models import Submission
from os_judge.celery import app


@app.task()
def run_judge(submission_id):
    submission = Submission.objects.get(id=submission_id)
    submission.state = 'judging'
    submission.save()
    directory = os.path.join('temp_judge', str(uuid.uuid4()))
    os.mkdir(directory)
    os.mkdir(os.path.join(directory, 'data'))
    os.mkdir(os.path.join(directory, 'report'))
    attachment_path = os.path.join(directory, 'attachment.zip')
    with open(attachment_path, "wb") as attachment_file:
        attachment_file.write(submission.attachment_content)
    unzip_result = subprocess.run(
        args=['unzip', '-q', 'attachment.zip', '-d', 'data'],
        cwd=directory,
        capture_output=True,
    )
    if unzip_result.returncode != 0:
        submission.state = 'fail to unzip'
        submission.error_log = unzip_result.stderr.decode('utf-8')
        submission.output_log = unzip_result.stdout.decode('utf-8')
        submission.judged_at = timezone.now()
        submission.save()
        shutil.rmtree(directory)
        return
    shutil.copy('judge-docker-compose.yml', os.path.join(directory, "docker-compose.yml"))
    judge_result = subprocess.run(
        args=['docker-compose', 'up', '--no-log-prefix'],
        cwd=directory,
        capture_output=True,
    )
    if judge_result.returncode == 0:
        submission.state = 'judged'
    else:
        submission.state = 'fail to judge'
    submission.error_log = judge_result.stderr.decode('utf-8')
    submission.output_log = judge_result.stdout.decode('utf-8')
    if len(submission.output_log) > settings.MAX_SUBMISSION_SIZE:
        submission.output_log = submission.output_log[:settings.MAX_SUBMISSION_SIZE]
    submission.judged_at = timezone.now()
    submission.log_tests = ''
    performed_tests = 0
    submission.passed_tests = 0
    for filename in os.listdir(os.path.join(directory, 'report')):
        file_path = os.path.join(directory, 'report', filename)
        if os.path.isfile(file_path) and filename.endswith('.txt'):
            with open(file_path, 'r') as file:
                lines = file.readlines()
            if len(lines) > 4:
                lines = lines[:4]
            file_result = '\n'.join(lines)
            submission.log_tests += file_result
            results = re.findall(
                pattern=r'Tests run: (\d*), Failures: (\d*), Errors: (\d*), Skipped: (\d*)',
                string=file_result,
            )
            if len(results) > 0:
                performed_tests += 1
                result = results[0]
                submission.passed_tests += int(result[0]) - int(result[1]) - int(result[2]) - int(result[3])
    submission.total_tests = settings.TEST_COUNT
    if performed_tests < settings.TEST_COUNT:
        submission.state = 'failed to run all tests'
    submission.save()
    subprocess.run(
        args=['docker-compose', 'rm', '-f'],
        cwd=directory,
        capture_output=True,
    )
    subprocess.run(
        args=['docker-compose', 'down', ],
        cwd=directory,
        capture_output=True,
    )
    shutil.rmtree(directory)
