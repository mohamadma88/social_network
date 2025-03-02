from rest_framework.test import APITestCase
from account.models import User
from django.urls import reverse, resolve
from friend import views


class TestUserListUrls(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create(username='1234', password='1234')

    def test_user_list_url(self):
        url = reverse('user_request')
        self.assertEqual(resolve(url).func.view_class, views.Userlist)

    def test_request_url(self):
        url = reverse('request_friend')
        self.assertEqual(resolve(url).func.view_class, views.Request)

    def test_request_list_url(self):
        url = reverse('request_list')
        self.assertEqual(resolve(url).func.view_class, views.RequestList)

    def test_accept_url(self):
        url = reverse('accept')
        self.assertEqual(resolve(url).func.view_class, views.Accept)
