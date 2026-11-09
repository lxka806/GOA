from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from rest_framework import status
from rest_framework.response import Response

from .models import Task
from .serializers import TaskSerializer


class TaskViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Task.objects.filter(task_owner=self.request.user)

        return Task.objects.filter(task_owner__isnull=True)

    def perform_create(self, serializer):
        task_owner = (
            self.request.user
            if self.request.user.is_authenticated
            else None
        )

        serializer.save(task_owner=task_owner)

    def destroy(self, request, *args, **kwargs):
        task = self.get_object()
        self.perform_destroy(task)

        return Response(status=status.HTTP_204_NO_CONTENT)