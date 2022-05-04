from rest_framework import viewsets
from blog.models import Post, Category, Tag, Comment
from .serializers import PostSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
