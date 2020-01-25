from django.shortcuts import render
from django_filters import rest_framework as filters
from django.contrib.auth.models import User

from rest_framework import viewsets
from rest_framework.generics import CreateAPIView 
from rest_framework.response import Response
from oauth2_provider.contrib.rest_framework import TokenHasScope
from .models import Post, Comment
from .serializers import UserSerializer, PostSerializer, CommentSerializer
# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer
	permission_classes = [TokenHasScope]
	required_scopes = ['read']

class UserRegisterView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = []

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    filterset_fields = ['post_id']
