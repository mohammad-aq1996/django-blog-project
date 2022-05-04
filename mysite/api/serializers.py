from rest_framework import serializers
from blog.models import Post, Category, Tag, Comment


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class CommentCategory(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
