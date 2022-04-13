from django.conf import settings
from django.core.management.base import BaseCommand
from django.db import transaction

from judge.models import Submission


class Command(BaseCommand):

    @transaction.atomic
    def handle(self, *args, **options):
        for submission in Submission.objects.all():
            if len(submission.output_log) > settings.MAX_SUBMISSION_SIZE:
                submission.output_log = submission.output_log[:settings.MAX_SUBMISSION_SIZE]
                submission.save()
