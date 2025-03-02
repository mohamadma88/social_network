from rest_framework import status
from rest_framework.test import APITestCase
from account.models import User
from post.models import Post, Comment
from rest_framework_simplejwt.tokens import RefreshToken
from django.urls import reverse


class TestPostList(APITestCase):

    @classmethod
    def setUpTestData(cls):
        cls.username = '1234'
        cls.password = 'test1234'
        cls.user = User.objects.create_user(username='1234', password='test1234')
        cls.post = Post.objects.create(title='life', caption='very goood ! ', user=cls.user)
        refresh = RefreshToken.for_user(cls.user)
        cls.token = str(refresh.access_token)

    def test_post_list(self):
        url = reverse('post_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class TestPostDetail(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.username = '1234'
        cls.password = 'test1234'
        cls.user = User.objects.create_user(username='1234', password='test1234')
        cls.post = Post.objects.create(title='life', caption='is goood', user=cls.user)
        refresh = RefreshToken.for_user(cls.user)
        cls.token = str(refresh.access_token)

    def test_post_detail_unauthorized(self):
        url = reverse('detail_post', args=(self.post.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_post_detail_authorized(self):
        url = reverse('detail_post', args=(self.post.id,))
        response = self.client.get(url, HTTP_AUTHORIZATION=f'Bearer {self.token}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.post.title)


class TestCreatePost(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.username = '1234'
        cls.password = 'test1234'
        cls.user = User.objects.create_user(username=cls.username, password=cls.password)
        cls.post = Post.objects.create(title='life', caption='is goood',user=cls.user)
        refresh = RefreshToken.for_user(cls.user)
        cls.token = str(refresh.access_token)

    def test_create_post_unauthorized(self):
        url = reverse('create_post')
        new_data = {
            'title': 'life ',
            'caption': 'is wonderful',
        }
        response = self.client.post(url, data=new_data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_post_authorized(self):
        url = reverse('create_post')
        new_data = {
                'title': 'Fan',
                'caption': 'Nice',

            }

        response = self.client.post(url, data=new_data, HTTP_AUTHORIZATION=f'Bearer {self.token}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class TestComment(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.username = '1234'
        cls.password = 'test1234'
        cls.user = User.objects.create(username=cls.username,password=cls.password)
        cls.post = Post.objects.create(title='life',caption='is good',user=cls.user)
        cls.comment = Comment.objects.create(post=cls.post,user=cls.user,text='post is good')
        refresh = RefreshToken.for_user(cls.user)
        cls.token = str(refresh.access_token)

    def test_comment(self):
        url = reverse('comment',args=[self.post.pk])
        new_data = {
            'text':'life is not bad',
        }
        response = self.client.post(url,data=new_data,HTTP_AUTHORIZATION=f'Bearer {self.token}')
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)

