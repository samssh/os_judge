from django.conf import settings
from rest_framework import serializers

from judge.models import Submission


class JudgeSerializer(serializers.ModelSerializer):
    sender = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    @staticmethod
    def validate_attachment(value):
        if value.size > settings.MAX_SUBMISSION_SIZE:
            raise serializers.ValidationError("file size in more than 500kb")
        return value

    def create(self, validated_data):
        attachment = validated_data['attachment']
        validated_data['attachment_content'] = attachment.read()
        attachment.seek(0)
        return super(JudgeSerializer, self).create(validated_data)

    class Meta:
        model = Submission
        fields = [
            'id',
            'created_at',
            'judged_at',
            'sender',
            'state',
            'attachment',
            'passed_tests',
            'total_tests',
            'master_grade',
            'log_tests',
            'output_log',
        ]
        read_only_fields = [
            'id',
            'created_at',
            'judged_at',
            'state',
            'passed_tests',
            'total_tests',
            'master_grade',
            'log_tests',
            'output_log',
        ]
