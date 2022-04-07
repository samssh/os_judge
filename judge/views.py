from rest_framework import mixins
from rest_framework import viewsets, permissions

from .execute_judge import run_judge
from .models import Submission
from judge.serializers import JudgeSerializer


class UploadViewSet(viewsets.ReadOnlyModelViewSet, mixins.CreateModelMixin):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = JudgeSerializer
    queryset = Submission.objects.none()

    def get_queryset(self):
        return Submission.objects.filter(sender=self.request.user)

    def perform_create(self, serializer):
        serializer.save()
        run_judge.delay(serializer.instance.id)
