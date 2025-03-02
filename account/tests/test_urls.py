from rest_framework.test import APISimpleTestCase
from django.urls import reverse, resolve
from account.views import UserView
from rest_framework_simplejwt.views import TokenObtainPairView


class TestUrls(APISimpleTestCase):
    def test_login(self):
        url = reverse('account:login')
        self.assertEqual(resolve(url).func.view_class, TokenObtainPairView)

    def test_profile_detail(self):
        url = reverse('account:profile')
        self.assertEqual(resolve(url).func.view_class, UserView)
