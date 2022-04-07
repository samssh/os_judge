from rest_framework import serializers

from judge.models import Submission


class JudgeSerializer(serializers.ModelSerializer):
    sender = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    def validate_attachment(self, value):
        if value.size > 500 * 1024:
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
