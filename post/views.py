
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Post
from rest_framework import status
from .serializers import Postserializers, CommentSerializer, LikeSerializer
from rest_framework.permissions import IsAuthenticated
from post.permissions import IsUserOrReadOnly
from rest_framework.parsers import MultiPartParser


class PostView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        try:
            post = Post.objects.get(pk=pk, user=request.user)
        except Post.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        ser = Postserializers(post)
        return Response(ser.data)

    def post(self, request):
        ser = Postserializers(data=request.data)
        if ser.is_valid():
            ser.save(user=request.user)
            return Response(ser.data)
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)


class PostCreateView(APIView):
    permission_classes = [IsAuthenticated,IsUserOrReadOnly]
    serializer_class = Postserializers
    parser_classes = [MultiPartParser]

    def post(self, request):
        serializer = Postserializers(data=request.data)
        if serializer.is_valid():
            serializer.validated_data['user'] = self.request.user
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)


class PostList(APIView):
    permission_classes = [IsUserOrReadOnly]

    def get(self, request):
        post = Post.objects.all()
        serializer = Postserializers(post, many=True)
        return Response(serializer.data)


class CommentView(APIView):
    permission_classes = [IsAuthenticated]

    def get_post(self, pk):
        try:
            return Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            return False

    def get(self, request, pk):
        post = self.get_post(pk)
        if not post:
            return Response(status=status.HTTP_404_NOT_FOUND)

        comments = post.comment.filter(is_approved=True)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

    def post(self, request, pk):
        post = self.get_post(pk)
        if not post:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(post=post, user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LikeView(APIView):
    permission_classes = [IsAuthenticated]

    def get_post(self, post_pk):
        try:
            return Post.objects.get(pk=post_pk)
        except Post.DoesNotExist:
            return False

    def get(self, request, post_pk):
        post = self.get_post(post_pk)
        if not post:
            return Response(status=status.HTTP_404_NOT_FOUND)

        likes = post.likes.filter(is_liked=True).count()
        return Response({'likes': likes})

    def post(self, request, post_pk):
        post = self.get_post(post_pk)
        if not post:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = LikeSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(post=post, user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
