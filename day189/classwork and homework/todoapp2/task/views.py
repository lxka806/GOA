from django.shortcuts import render, redirect
from .utils import create_task, delete_task
from .models import Task


def add_task(request):
    if request.method == "POST":
        create_task(request.POST)
        return redirect("main")

    tasks = Task.objects.all()

    return render(request, "index.html", {
        "tasks": tasks
    })


def delete(request, id):
    delete_task(id)
    return redirect("main")