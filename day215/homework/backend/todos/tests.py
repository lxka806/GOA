from rest_framework import status
from rest_framework.test import APITestCase
from .models import Task


class TaskApiTests(APITestCase):
    def test_create_task(self):
        response = self.client.post(
            "/api/tasks/",
            {"title": "Plan the week"},
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["title"], "Plan the week")
        self.assertFalse(response.data["completed"])
        self.assertEqual(Task.objects.count(), 1)

    def test_edit_task(self):
        task = Task.objects.create(title="Old title")

        response = self.client.patch(
            f"/api/tasks/{task.id}/",
            {"title": "Updated title"},
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Updated title")
        task.refresh_from_db()
        self.assertEqual(task.title, "Updated title")

    def test_edit_missing_task_returns_not_found(self):
        response = self.client.patch(
            "/api/tasks/999/",
            {"title": "Updated title"},
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_delete_task(self):
        task = Task.objects.create(title="Remove this task")

        response = self.client.delete(f"/api/tasks/{task.id}/")

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Task.objects.filter(id=task.id).exists())

    def test_delete_missing_task_returns_not_found(self):
        response = self.client.delete("/api/tasks/999/")

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
