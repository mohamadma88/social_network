from django.urls import path
from .views import (Userlist, Request, RequestList, Accept)

urlpatterns = [
    path('user/list', Userlist.as_view(), name='user_request'),
    path('request', Request.as_view(), name='request_friend'),
    path('request/list', RequestList.as_view(), name='request_list'),
    path('accept', Accept.as_view(), name='accept'),
]

