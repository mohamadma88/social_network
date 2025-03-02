from django.urls import path
from .views import PostView, PostList, PostCreateView, CommentView , LikeView

name_app = 'post'
urlpatterns = [
    path('', PostView.as_view(), name='post'),
    path('detail/<int:pk>/', PostView.as_view(), name='detail_post'),
    path('list/', PostList.as_view(), name='post_list'),
    path('create/', PostCreateView.as_view(), name='create_post'),
    path('post/<int:pk>/comment', CommentView.as_view(), name='comment'),
    path('post/<int:post_pk>/likes/', LikeView.as_view(), name='like'),
]
