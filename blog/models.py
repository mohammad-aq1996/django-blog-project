from django.contrib.auth.models import User
from django.db import models
from ckeditor.fields import RichTextField
from django.shortcuts import reverse


class Post(models.Model):
    """
    creating a table for blog post in database
    """
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author', default=1)
    title = models.CharField(max_length=150)
    content = RichTextField()
    image = models.ImageField(upload_to='post')
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='category')
    tags = models.ManyToManyField('Tag', related_name='tags')
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)

    def get_absolute_url(self):
        return reverse('blog:post_detail', kwargs={'pk': self.id})

    def __str__(self):
        return self.title


class Category(models.Model):
    """
    creating a table for categories in database
    relation: category 1:1 post
    """
    name = models.CharField(max_length=150)
    slug = models.SlugField()

    def __str__(self):
        return self.name


class Tag(models.Model):
    """
    creating a table for tags in database
    relation: many to many with post
    """
    name = models.CharField(max_length=150)
    slug = models.SlugField()

    def __str__(self):
        return self.name


class Blogger(models.Model):
    """
    creating a table for blogger profile in database
    relation: blogger 1:1 user
    """
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    describe = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to='post')

    def __str__(self):
        return self.author.username


class Comment(models.Model):
    """
    creating a table for comments in database
    relation: post 1:N comments
    """
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=150)
    email = models.EmailField()
    title = models.CharField(max_length=250)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.email

















