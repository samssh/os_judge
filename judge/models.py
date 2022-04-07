import os
import uuid

from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


def get_uploaded_attachment_path(instance, filename):
    filename, file_extension = os.path.splitext(filename)
    return os.path.join(
        'upload',
        timezone.now().strftime("%Y/%m/%d"),
        "%s%s" % (uuid.uuid4(), file_extension),
    )


class Submission(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    judged_at = models.DateTimeField(null=True, blank=True)
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='submissions')
    state = models.CharField(default='pending', max_length=100)
    attachment = models.FileField(upload_to=get_uploaded_attachment_path)
    attachment_content = models.BinaryField(editable=True)
    passed_tests = models.IntegerField(default=-1)
    total_tests = models.IntegerField(default=-1)
    master_grade = models.IntegerField(default=-1)
    output_log = models.TextField(null=True, blank=True)
    error_log = models.TextField(null=True, blank=True)
    log_tests = models.TextField(null=True, blank=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return '{} at {}'.format(self.sender.username, self.created_at)
