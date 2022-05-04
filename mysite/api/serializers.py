from rest_framework import serializers
from blog.models import Post, Category, Tag, Comment


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
