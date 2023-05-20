
from rest_framework.test import APITestCase

from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()


class TestUserProfile(APITestCase):
    url = reverse('user-profile')

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

    def test_get_user_profile(self):
        headers = {"HTTP_AUTHORIZATION": f"Bearer {self.user.tokens.get('access')}"}
        response = self.client.get(self.url, **headers)
        self.assertEqual(response.status_code, 200)
        self.assertListEqual(list(response.data.keys()), [
            "id",
            "full_name",
            "username",
            "phone",
            "email",
            "photo"
        ])
        self.assertEqual(response.data['id'], self.user.id)
        self.assertEqual(response.data['full_name'], self.user.full_name)
        self.assertEqual(response.data['username'], self.user.username)
        self.assertEqual(response.data['phone'], self.user.phone)
        self.assertEqual(response.data['email'], self.user.email)
        self.assertEqual(response.data['photo'], self.user.photo)

    def test_get_user_profile_no_auth(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json()['detail'], 'Authentication credentials were not provided.')
