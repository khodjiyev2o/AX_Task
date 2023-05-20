from rest_framework.test import APITestCase

from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()


class TestUserUpdate(APITestCase):
    url = reverse("user-update")

    def setUp(self):
        self.user = User.objects.create_user(
            phone="+998972081018",
            password="12345678",
            first_name="Samandar",
            last_name="Hojiev",
            middle_name="Ulugbek",
            username="khodjiyev2o",
            date_of_birth='2004-04-20',
            email="samandarkhodjiyev@gmail.com",
        )
        self.admin = User.objects.create_superuser(email='admin@gmail.com', password='test_password')
        self.maxDiff = None

    def test_update_user(self):
        headers = {"HTTP_AUTHORIZATION": f"Bearer {self.user.tokens.get('access')}"}
        data = {
            "first_name": "Updated name",
            "username": "proger03",
            "date_of_birth": "2003-05-20",
        }
        response = self.client.patch(self.url, data=data, **headers)
        expected_response = {
            "id": self.user.id,
            "first_name": data['first_name'],
            "last_name": self.user.last_name,
            "username": data['username'],
            "email": self.user.email,
            "date_of_birth": data['date_of_birth'],
            "photo": None
        }
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), expected_response)

    def test_update_user_no_auth(self):
        response = self.client.patch(self.url)
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json()['detail'], 'Authentication credentials were not provided.')