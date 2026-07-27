from django.shortcuts import render, redirect
from .models import Task

def add_task(req):
    if req.method == "POST":
        task_name = req.POST.get("task_name")

        new_task = Task(task_name=task_name)
        new_task.save()

        return redirect("home")

    tasks = Task.objects.all()
    return render(req, "home.html", {"tasks": tasks})


def delete_task(req, id):
    delete_task = Task.objects.get(id=id)
    delete_task.delete()
    return redirect("home")