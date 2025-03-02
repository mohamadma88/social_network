from rest_framework import serializers
from .models import Post, Comment, Like


class Postserializers(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Post
        fields = ('user','title', 'caption', )
        extra_kwargs = {
            'user': {'read_only': True},
        }


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('post', 'user', 'text')
        extra_kwargs = {
            'post': {'read_only': True},
            'user': {'read_only': True}
        }


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ('post', 'user', 'is_liked')
        extra_kwargs = {
            'post': {'read_only': True},
            'user': {'read_only': True},
            'is_liked': {'required': False}
        }
