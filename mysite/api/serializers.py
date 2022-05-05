from rest_framework import serializers
from blog.models import Post, Category, Tag, Comment


class PostSerializer(serializers.ModelSerializer):
    def get_author(self, obj):
        return obj.author.username

    def get_tag(self, obj):
        return [tag.name for tag in obj.tags.all()]

    def get_category(self, obj):
        return obj.category.name

    author = serializers.SerializerMethodField('get_author')
    tags = serializers.SerializerMethodField('get_tag')
    category = serializers.SerializerMethodField('get_category')

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
