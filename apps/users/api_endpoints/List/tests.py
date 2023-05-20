from rest_framework.test import APITestCase

from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()


class TestUserList(APITestCase):
    url = reverse('users-list')

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

    def test_get_users_list_admin_user(self):
        headers = {"HTTP_AUTHORIZATION": f"Bearer {self.admin.tokens.get('access')}"}
        response = self.client.get(self.url, **headers)
        self.assertEqual(response.status_code, 200)
        self.assertListEqual(list(response.data.keys()), ['count', 'next', 'previous', 'results'])
        self.assertListEqual(list(response.data['results'][0].keys()), [
            'id',
            'first_name',
            'last_name',
            'phone',
            'email',
            'is_active'
        ])
        self.assertEqual(response.data['results'][0]['id'], self.user.id)
        self.assertEqual(response.data['results'][0]['first_name'], self.user.first_name)
        self.assertEqual(response.data['results'][0]['last_name'], self.user.last_name)
        self.assertEqual(response.data['results'][0]['email'], self.user.email)
        self.assertEqual(response.data['results'][0]['is_active'], self.user.is_active)

    def test_get_users_list_valid_search_email(self):
        headers = {"HTTP_AUTHORIZATION": f"Bearer {self.admin.tokens.get('access')}"}
        response = self.client.get(f'{self.url}?search={self.user.first_name}', **headers)
        self.assertEqual(response.status_code, 200)
        self.assertListEqual(list(response.data.keys()), ['count', 'next', 'previous', 'results'])
        self.assertListEqual(list(response.data['results'][0].keys()), [
            'id',
            'first_name',
            'last_name',
            'phone',
            'email',
            'is_active'
        ])
        self.assertEqual(response.data['results'][0]['id'], self.user.id)
        self.assertEqual(response.data['results'][0]['first_name'], self.user.first_name)
        self.assertEqual(response.data['results'][0]['last_name'], self.user.last_name)
        self.assertEqual(response.data['results'][0]['email'], self.user.email)
        self.assertEqual(response.data['results'][0]['is_active'], self.user.is_active)

    def test_get_users_list_valid_search_username(self):
        headers = {"HTTP_AUTHORIZATION": f"Bearer {self.admin.tokens.get('access')}"}
        response = self.client.get(f'{self.url}?search={self.user.username}', **headers)
        self.assertEqual(response.status_code, 200)
        self.assertListEqual(list(response.data.keys()), ['count', 'next', 'previous', 'results'])
        self.assertListEqual(list(response.data['results'][0].keys()), [
            'id',
            'first_name',
            'last_name',
            'phone',
            'email',
            'is_active'
        ])
        self.assertEqual(response.data['results'][0]['id'], self.user.id)
        self.assertEqual(response.data['results'][0]['first_name'], self.user.first_name)
        self.assertEqual(response.data['results'][0]['last_name'], self.user.last_name)
        self.assertEqual(response.data['results'][0]['email'], self.user.email)
        self.assertEqual(response.data['results'][0]['is_active'], self.user.is_active)

    def test_get_users_list_valid_filter_is_staff(self):
        headers = {"HTTP_AUTHORIZATION": f"Bearer {self.admin.tokens.get('access')}"}
        response = self.client.get(f'{self.url}?is_staff={self.user.is_staff}', **headers)
        self.assertEqual(response.status_code, 200)
        self.assertListEqual(list(response.data.keys()), ['count', 'next', 'previous', 'results'])
        self.assertListEqual(list(response.data['results'][0].keys()), [
            'id',
            'first_name',
            'last_name',
            'phone',
            'email',
            'is_active'
        ])
        self.assertEqual(response.data['results'][0]['id'], self.user.id)
        self.assertEqual(response.data['results'][0]['first_name'], self.user.first_name)
        self.assertEqual(response.data['results'][0]['last_name'], self.user.last_name)
        self.assertEqual(response.data['results'][0]['email'], self.user.email)
        self.assertEqual(response.data['results'][0]['is_active'], self.user.is_active)

    def test_get_users_list_valid_filter_is_active(self):
        headers = {"HTTP_AUTHORIZATION": f"Bearer {self.admin.tokens.get('access')}"}
        response = self.client.get(f'{self.url}?is_active={self.user.is_active}', **headers)
        self.assertEqual(response.status_code, 200)
        self.assertListEqual(list(response.data.keys()), ['count', 'next', 'previous', 'results'])
        self.assertListEqual(list(response.data['results'][0].keys()), [
            'id',
            'first_name',
            'last_name',
            'phone',
            'email',
            'is_active'
        ])
        self.assertEqual(response.data['results'][0]['id'], self.user.id)
        self.assertEqual(response.data['results'][0]['first_name'], self.user.first_name)
        self.assertEqual(response.data['results'][0]['last_name'], self.user.last_name)
        self.assertEqual(response.data['results'][0]['email'], self.user.email)
        self.assertEqual(response.data['results'][0]['is_active'], self.user.is_active)

    def test_get_users_list_invalid_search(self):
        headers = {"HTTP_AUTHORIZATION": f"Bearer {self.admin.tokens.get('access')}"}
        response = self.client.get(f'{self.url}?search=invalid_search@gmail.com', **headers)
        self.assertEqual(response.status_code, 200)
        self.assertListEqual(list(response.data.keys()), ['count', 'next', 'previous', 'results'])
        self.assertEqual(response.data['next'], None)
        self.assertEqual(response.data['previous'], None)
        self.assertEqual(response.data['results'], [])

    def test_get_users_list_invalid_filter_is_staff(self):
        headers = {"HTTP_AUTHORIZATION": f"Bearer {self.admin.tokens.get('access')}"}
        response = self.client.get(f'{self.url}?is_staff=True&is_superuser=False', **headers)
        self.assertEqual(response.status_code, 200)
        self.assertListEqual(list(response.data.keys()), ['count', 'next', 'previous', 'results'])
        self.assertEqual(response.data['next'], None)
        self.assertEqual(response.data['previous'], None)
        self.assertEqual(response.data['results'], [])

    def test_get_users_list_invalid_filter_is_active(self):
        headers = {"HTTP_AUTHORIZATION": f"Bearer {self.admin.tokens.get('access')}"}
        response = self.client.get(f'{self.url}?is_active=False', **headers)
        self.assertEqual(response.status_code, 200)
        self.assertListEqual(list(response.data.keys()), ['count', 'next', 'previous', 'results'])
        self.assertEqual(response.data['next'], None)
        self.assertEqual(response.data['previous'], None)
        self.assertEqual(response.data['results'], [])

    def test_get_profile_no_authentication(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json()['detail'], 'Authentication credentials were not provided.')

    def test_get_profile_not_admin_user(self):
        headers = {"HTTP_AUTHORIZATION": f"Bearer {self.user.tokens.get('access')}"}
        response = self.client.get(self.url, **headers)
        self.assertEqual(response.status_code, 403)
        self.assertEqual(response.json()['detail'], 'You do not have permission to perform this action.')
