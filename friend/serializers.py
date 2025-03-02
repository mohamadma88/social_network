from rest_framework import serializers
from account.models import User


class UserListSerializer(serializers.Serializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'avatar')
