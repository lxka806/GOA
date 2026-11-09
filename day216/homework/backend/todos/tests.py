from rest_framework import status
from rest_framework.test import APIClient, APITestCase
from django.contrib.auth import get_user_model
from .models import Task


User = get_user_model()


class TaskApiTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="owner", password="Example-pass-123!")
        self.other_user = User.objects.create_user(
            username="someone-else",
            password="Example-pass-456!",
        )
        self.client.force_authenticate(user=self.user)

    def test_create_task(self):
        response = self.client.post(
            "/api/tasks/",
            {"title": "Plan the week"},
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["title"], "Plan the week")
        self.assertFalse(response.data["completed"])
        self.assertEqual(response.data["task_owner"], self.user.id)
        self.assertEqual(Task.objects.count(), 1)
        self.assertEqual(Task.objects.get().task_owner, self.user)

    def test_create_task_ignores_submitted_owner(self):
        response = self.client.post(
            "/api/tasks/",
            {"title": "My task", "task_owner": self.other_user.id},
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["task_owner"], self.user.id)

    def test_list_tasks_only_includes_current_user_tasks(self):
        own_task = Task.objects.create(title="My task", task_owner=self.user)
        Task.objects.create(title="Other task", task_owner=self.other_user)

        response = self.client.get("/api/tasks/")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual([task["id"] for task in response.data], [own_task.id])

    def test_cannot_modify_another_users_task(self):
        task = Task.objects.create(title="Private task", task_owner=self.other_user)

        response = self.client.patch(
            f"/api/tasks/{task.id}/",
            {"title": "Changed"},
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_edit_task(self):
        task = Task.objects.create(title="Old title", task_owner=self.user)

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
        task = Task.objects.create(title="Remove this task", task_owner=self.user)

        response = self.client.delete(f"/api/tasks/{task.id}/")

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Task.objects.filter(id=task.id).exists())

    def test_delete_missing_task_returns_not_found(self):
        response = self.client.delete("/api/tasks/999/")

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_tasks_require_authentication(self):
        self.client.force_authenticate(user=None)

        response = self.client.get("/api/tasks/")

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class AuthenticationApiTests(APITestCase):
    def test_registration_requires_csrf_token(self):
        client = APIClient(enforce_csrf_checks=True)
        registration_data = {
            "username": "protected-user",
            "password": "Example-pass-123!",
        }

        rejected = client.post(
            "/api/auth/register/",
            registration_data,
            format="json",
        )
        self.assertEqual(rejected.status_code, status.HTTP_403_FORBIDDEN)

        client.get("/api/auth/csrf/")
        csrf_token = client.cookies["csrftoken"].value
        accepted = client.post(
            "/api/auth/register/",
            registration_data,
            format="json",
            HTTP_X_CSRFTOKEN=csrf_token,
        )
        self.assertEqual(accepted.status_code, status.HTTP_201_CREATED)

    def test_register_creates_user_and_starts_session(self):
        response = self.client.post(
            "/api/auth/register/",
            {"username": "new-user", "password": "Example-pass-123!"},
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.json()["username"], "new-user")
        self.assertTrue(User.objects.filter(username="new-user").exists())

        current_user = self.client.get("/api/auth/user/")
        self.assertEqual(current_user.json()["username"], "new-user")

    def test_login_and_logout(self):
        User.objects.create_user(username="existing-user", password="Example-pass-123!")

        login_response = self.client.post(
            "/api/auth/login/",
            {"username": "existing-user", "password": "Example-pass-123!"},
            format="json",
        )
        self.assertEqual(login_response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            self.client.get("/api/auth/user/").json()["username"],
            "existing-user",
        )

        logout_response = self.client.post("/api/auth/logout/", {}, format="json")
        self.assertEqual(logout_response.status_code, status.HTTP_200_OK)
        self.assertIsNone(self.client.get("/api/auth/user/").json()["username"])

    def test_login_rejects_invalid_credentials(self):
        response = self.client.post(
            "/api/auth/login/",
            {"username": "missing", "password": "wrong"},
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
