from rest_framework.test import APITestCase
from account.models import User, Profile
from django.utils.translation import gettext_lazy as _


class AuthorModelTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create(username='mohamad')

    def test_username_label(self):
        field_label = self.user._meta.get_field('username').verbose_name
        self.assertEqual(field_label, _('username'))

    def test_object_name_is_last_name_comma_first_name(self):
        expected_object_name = f'{self.user.username}'
        self.assertEqual(str(self.user), expected_object_name)

    def test_str_method(self):
        expected_result = self.user.username
        self.assertEqual(self.user.__str__(), expected_result)
