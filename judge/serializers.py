from rest_framework import serializers

from judge.models import Submission


class JudgeSerializer(serializers.ModelSerializer):
    sender = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

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
        ]
        read_only_fields = [
            'id',
            'created_at',
            'judged_at',
            'state',
            'passed_tests',
            'total_tests',
            'log_tests',
            'master_grade',
        ]
