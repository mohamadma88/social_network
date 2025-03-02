from rest_framework.test import APITestCase
from account.models import User
from post.models import Post, Comment
from django.utils.translation import gettext_lazy as _


class PostModelTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(username='1234')
        cls.post = Post.objects.create(title='life', caption='is good', user=cls.user)

    def test_title_label(self):
        field_label = self.post._meta.get_field('title').verbose_name
        self.assertEqual(field_label, _('title'))

    def test_caption_label(self):
        field_label = self.post._meta.get_field('caption').verbose_name
        self.assertEqual(field_label, _('caption'))

    def test_str_method(self):
        expect_result = self.post.title
        self.assertEqual(self.post.__str__(), expect_result)


class CommentModelTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(username='1234')
        cls.post = Post.objects.create(title='test title comment-post', caption='test caption comment-post',
                                       user=cls.user)
        cls.comment = Comment.objects.create(post=cls.post, user=cls.user, text='the post is very goood')

    def test_text_label(self):
        field_label = self.comment._meta.get_field(_('text')).verbose_name
        self.assertEqual(field_label, _('text'))

    def test__str__method(self):
        field_label = self.comment.text
        self.assertEqual(self.comment.__str__(),field_label)