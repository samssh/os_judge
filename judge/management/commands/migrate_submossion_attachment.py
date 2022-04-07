from django.core.management.base import BaseCommand
from django.db import transaction

from judge.models import Submission


class Command(BaseCommand):

    @transaction.atomic
    def handle(self, *args, **options):
        for submission in Submission.objects.all():
            submission.attachment_content = submission.attachment.read()
            submission.save()
