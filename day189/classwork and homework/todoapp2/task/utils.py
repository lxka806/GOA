from .models import Task


def create_task(req_post):
    Task.objects.create(
        task_name=req_post.get("task_name")
    )


def delete_task(id):
    task = Task.objects.get(id=id)
    task.delete()