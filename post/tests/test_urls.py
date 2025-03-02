from rest_framework.test import APITestCase
from account.models import User
from post.models import Post , Comment ,Like
from django.urls import reverse, resolve
from post import views


class TestUrls(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.username = User.objects.create(username='1234', password='1234')
        cls.post = Post.objects.create(title='test url', caption='test url 2', user=cls.username)
        cls.comment = Comment.objects.create(text='test comment',post=cls.post,user=cls.username)
        cls.like = Like.objects.create(post=cls.post,user=cls.username , is_like=True)

    def test_post_url(self):
        url = reverse('post')
        self.assertEqual(resolve(url).func.view_class, views.PostView)

    def test_post_detail_url(self):
        url = reverse('detail_post', args=[self.post.pk])
        self.assertEqual(resolve(url).func.view_class, views.PostView)

    def test_post_list_url(self):
        url = reverse('post_list')
        self.assertEqual(resolve(url).func.view_class,views.PostList)

    def test_comment_url(self):
        url=reverse('comment',args=[self.comment.pk])
        self.assertEqual(resolve(url).func.view_class,views.CommentView)

    def test_like_url(self):
        url = reverse('like',args=[self.like.pk])
        self.assertEqual(resolve(url).func.view_class,views.LikeView)
