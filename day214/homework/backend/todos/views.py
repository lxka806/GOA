from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Task
from .serializers import TaskSerializer


@api_view(['GET', 'POST'])
def task_view(request):
    if request.method == 'GET':
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = TaskSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
        
        return Response(serializer.data)