from django.contrib.auth.password_validation import password_changed
from rest_framework.test import APITestCase
from account.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from friend.models import Friend


class TestUserListView(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.username = '1234'
        cls.password = '1234'
        cls.user = User.objects.create(username='1234', password='1234')
        refresh = RefreshToken.for_user(cls.user)
        cls.token = str(refresh.access_token)

    def test_profile_auth(self):
        url = reverse('user_request')
        response = self.client.get(url, HTTP_AUTHORIZATION=f'Bearer {self.token}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        if isinstance(response.data, list) and len(response.data) > 0:
            self.assertTrue('username' in response.data[0])
            self.assertEqual(response.data[0]['username'], self.username)


class TestRequest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user1 = User.objects.create_user(username='user1', password='password')
        cls.user2 = User.objects.create_user(username='user2', password='password')
        refresh = RefreshToken.for_user(cls.user1)
        cls.token = str(refresh.access_token)

    def test_request(self):
        url = reverse('request_friend')
        data = {'user': self.user2.id}

        response = self.client.post(url, data=data, HTTP_AUTHORIZATION=f'Bearer {self.token}')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data, {'response': 'Request sent'})
        self.assertTrue(Friend.objects.filter(req_from=self.user1, req_to=self.user2).exists())

    def test_request_non_exist_user(self):
        url = reverse('request_friend')
        data = {'user': 9999}

        response = self.client.post(url, data=data, HTTP_AUTHORIZATION=f'Bearer {self.token}')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

