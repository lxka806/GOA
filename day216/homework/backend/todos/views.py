import json

from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_protect
from django.views.decorators.http import require_GET, require_POST
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Task
from .serializers import RegistrationSerializer, TaskSerializer


@ensure_csrf_cookie
@require_GET
def csrf_token(request):
    return JsonResponse({"detail": "CSRF cookie set."})


@require_GET
def current_user(request):
    username = request.user.username if request.user.is_authenticated else None
    return JsonResponse({"username": username})


@csrf_protect
@require_POST
def register(request):
    serializer = RegistrationSerializer(data=request_json(request))
    if not serializer.is_valid():
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    user = serializer.save()
    login(request, user)
    return JsonResponse({"username": user.username}, status=status.HTTP_201_CREATED)


@csrf_protect
@require_POST
def log_in(request):
    data = request_json(request)
    username = data.get("username")
    password = data.get("password")
    if not isinstance(username, str) or not isinstance(password, str):
        return JsonResponse(
            {"detail": "Username and password are required."},
            status=status.HTTP_400_BAD_REQUEST,
        )
    user = authenticate(request, username=username, password=password)
    if user is None:
        return JsonResponse(
            {"detail": "Invalid username or password."},
            status=status.HTTP_400_BAD_REQUEST,
        )
    login(request, user)
    return JsonResponse({"username": user.username})


@csrf_protect
@require_POST
def log_out(request):
    logout(request)
    return JsonResponse({"detail": "Logged out."})


def request_json(request):
    try:
        data = json.loads(request.body)
    except (json.JSONDecodeError, UnicodeDecodeError):
        return {}
    return data if isinstance(data, dict) else {}


@api_view(["GET", "POST"])
def get_tasks(request):
    if request.method == "POST":
        serializer = TaskSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(task_owner=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    tasks = Task.objects.filter(task_owner=request.user)
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)


@api_view(["PATCH", "PUT", "DELETE"])
def update_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id, task_owner=request.user)
    if request.method == "DELETE":
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    serializer = TaskSerializer(
        task,
        data=request.data,
        partial=request.method == "PATCH",
    )
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)