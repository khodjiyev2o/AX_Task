from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status

User = get_user_model()


class TestCreateUser(APITestCase):
    url = reverse('user-create')

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
        self.maxDiff = None

    def test_create_user_with_valid_data(self):
        data = {
            "email": 'myemail@gmail.com',
            "password": '1112312',
        }
        response = self.client.post(self.url, data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.json(), data)

    def test_create_user_with_invalid_email(self):
        data = {
            "email": 'myemail@.co',
            "password": '1112312',
        }
        response = self.client.post(self.url, data=data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.json()['email'], ['Enter a valid email address.'])

    def test_create_user_with_existing_email(self):
        data = {
            "email": self.user.email,
            "password": '1112312',
        }
        response = self.client.post(self.url, data=data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.json()['email'], ['User with this Email already exists.'])
