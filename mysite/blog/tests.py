from unicodedata import category
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse, resolve
from .models import Post, Category, Tag, Comment
from django.core.files.uploadedfile import SimpleUploadedFile


class PostTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_superuser(
            username='test',
            email='test@gmail.com',
            password='Agl19902022cx',
        )
        self.category = Category.objects.create(
            name='Jenaei',
            slug='jenaei',
        )
        tag1 = Tag.objects.create(
            name='Jen',
            slug='jen',
        )        
        tag2 = Tag.objects.create(
            name='Gen',
            slug='gen',
        )
        self.post = Post.objects.create(
            author = self.user,
            title = 'Harru Potter',
            content = 'test test test test test test test test test test test test test test test test test test test test test test ',
            image = 'blog/BioShock.jpg',
            category = self.category,
            created_at = '2022-02-22 14:26:00',
            published_at ='2022-02-25 22:26:00',
        )
        self.post.tags.set([tag1, tag2])

    def test_post_listing(self):
        self.assertEqual(f'{self.post.author}', 'test')
        self.assertEqual(f'{self.post.title}', 'Harru Potter')
        self.assertEqual(f'{self.post.content}', 'test test test test test test test test test test test test test test test test test test test test test test ')
        self.assertEqual(f'{self.post.image}', 'blog/BioShock.jpg')
        self.assertEqual(f'{self.post.category}', 'Jenaei')
        self.assertEqual(self.post.tags.count(), 2)
        self.assertEqual(f'{self.post.created_at}', '2022-02-22 14:26:00')
        self.assertEqual(f'{self.post.published_at}', '2022-02-25 22:26:00')
