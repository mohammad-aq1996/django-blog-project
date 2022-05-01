from django.contrib.auth.models import User
from django.db import models
from ckeditor.fields import RichTextField
from django.shortcuts import reverse
from django.utils import timezone
from jalali_date import datetime2jalali


class Post(models.Model):
    """
    creating a table for blog post in database
    """
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author', verbose_name='نویسنده', default=1)
    title = models.CharField(max_length=150, verbose_name='عنوان')
    content = RichTextField(verbose_name='محتوا')
    image = models.ImageField(upload_to='post', verbose_name='تصویر')
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='category', verbose_name='دسته بندی')
    tags = models.ManyToManyField('Tag', related_name='tags', verbose_name='تگ ها')
    created_at = models.DateTimeField(default=timezone.now, verbose_name='زمان نوشته شدن')
    published_at = models.DateTimeField(blank=True, null=True, verbose_name='زمان انتشار')

    class Meta:
        verbose_name = 'پست'
        verbose_name_plural = 'پست ها'
        
    def get_published_jalali(self):
        return datetime2jalali(self.published_at)

    def get_absolute_url(self):
        return reverse('blog:post_detail', kwargs={'pk': self.id})

    def __str__(self):
        return self.title


class Category(models.Model):
    """
    creating a table for categories in database
    relation: category 1:1 post
    """
    name = models.CharField(max_length=150, verbose_name='عنوان دسته بندی')
    slug = models.SlugField()

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'

    def __str__(self):
        return self.name


class Tag(models.Model):
    """
    creating a table for tags in database
    relation: many to many with post
    """
    name = models.CharField(max_length=150, verbose_name='عنوان برچسب')
    slug = models.SlugField()

    class Meta:
        verbose_name = 'برچسب'
        verbose_name_plural = 'برچسب ها'

    def __str__(self):
        return self.name


# class Blogger(models.Model):
#     """
#     creating a table for blogger profile in database
#     relation: blogger 1:1 user
#     """
#     author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user', verbose_name='نویسنده')
#     describe = models.CharField(max_length=100, verbose_name='عنوان')
#     content = RichTextField(verbose_name='توضیحات')
#     image = models.ImageField(upload_to='post', verbose_name='تصویر')
#
#     class Meta:
#         verbose_name = 'مدیر وبلاگ'
#         verbose_name_plural = 'مدیر وبلاگ'
#
#     def __str__(self):
#         return self.author.username


class Comment(models.Model):
    """
    creating a table for comments in database
    relation: post 1:N comments
    """
    STATUS_CHOICE = [
        ('draft', 'Draft'),
        ('publish', 'Publish')
    ]
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments', verbose_name='پست')
    name = models.CharField(max_length=150, verbose_name='نام')
    email = models.EmailField(verbose_name='ایمیل')
    title = models.CharField(max_length=250, verbose_name='عنوان')
    message = models.TextField(verbose_name='پیام')
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True, verbose_name='زمان ارسال')
    status = models.CharField(max_length=8, choices=STATUS_CHOICE, default='draft', verbose_name='وضغیت')

    class Meta:
        verbose_name = 'نظر'
        verbose_name_plural = 'نظرات'

    def __str__(self):
        return self.email

    def get_comment_jalali(self):
        return datetime2jalali(self.created_at)
















