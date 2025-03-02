from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .serializers import UserListSerializer
from rest_framework.views import Response
from rest_framework import status
from account.models import User
from .models import Friend


class Userlist(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        ser = UserListSerializer(many=True)
        return Response(ser.data)


class Request(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.data.get('user')

        try:
            user = User.objects.get(pk=user)
        except User.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        Friend.objects.get_or_create(req_from=request.user, req_to=user)
        return Response({'response': 'Request sent'}, status=status.HTTP_201_CREATED)


class RequestList(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        friendship = Friend.objects.filter(request_to=request.user)
        user = [friend.request_from for friend in friendship]
        serializer = UserListSerializer(user, many=True)
        return Response(serializer.data)


class Accept(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.data.get('user')

        try:
            user = User.objects.get(pk=user)
            friend = Friend.objects.get(req_from=user, req_to=request.user, is_accept=False)
        except (user.DoesNotExist, friend.DoesNotExist):
            return Response(status=status.HTTP_400_BAD_REQUEST)
        friend.is_accept = True
        friend.save()
        return Response({'response': 'accept'})
