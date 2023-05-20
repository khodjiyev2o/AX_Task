from rest_framework.test import APITestCase

from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()


class TestUserDetail(APITestCase):

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

    def test_get_user_detail_admin_user(self):
        headers = {"HTTP_AUTHORIZATION": f"Bearer {self.admin.tokens.get('access')}"}
        url = reverse('user-detail-by-id', kwargs={'pk': self.user.id})
        response = self.client.get(url, **headers)
        self.assertEqual(response.status_code, 200)
        self.assertListEqual(list(response.data.keys()), [
            'id',
            'first_name',
            'last_name',
            'middle_name',
            'username',
            'phone',
            'email',
            'photo',
            'date_of_birth',
            'is_active',
            'is_staff',
        ])
        self.assertEqual(response.data['id'], self.user.id)
        self.assertEqual(response.data['first_name'], self.user.first_name)
        self.assertEqual(response.data['last_name'], self.user.last_name)
        self.assertEqual(response.data['middle_name'], self.user.middle_name)
        self.assertEqual(response.data['username'], self.user.username)
        self.assertEqual(response.data['phone'], self.user.phone)
        self.assertEqual(response.data['email'], self.user.email)
        self.assertEqual(response.data['photo'], self.user.photo)
        self.assertEqual(response.data['date_of_birth'], self.user.date_of_birth)
        self.assertEqual(response.data['is_active'], self.user.is_active)
        self.assertEqual(response.data['is_staff'], self.user.is_staff)

    def test_get_profile_no_authentication(self):
        url = reverse('user-detail-by-id', kwargs={'pk': self.user.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json()['detail'], 'Authentication credentials were not provided.')

    def test_get_profile_not_admin_user(self):
        url = reverse('user-detail-by-id', kwargs={'pk': self.user.id})
        headers = {"HTTP_AUTHORIZATION": f"Bearer {self.user.tokens.get('access')}"}
        response = self.client.get(url, **headers)
        self.assertEqual(response.status_code, 403)
        self.assertEqual(response.json()['detail'], 'You do not have permission to perform this action.')

    def test_user_model_str_method(self):
        self.assertEqual(str(self.user), self.user.email)

    def test_user_model_full_name_method(self):
        self.assertEqual(self.user.full_name, f"{self.user.first_name} {self.user.last_name}")

    def test_user_model_tokens_method(self):
        self.assertEqual(list(self.user.tokens.keys()), ['access', 'refresh'])
