from django.test import TestCase
from .models import Comment


class TestComment(TestCase):
    def setUp(self):
        self.comment = Comment.objects.create(
            name = 'mamali',
            email = 'mamal@gmail.com',
            subject = 'Good Idea',
            message = "You\'r blog is awsome.",
        )

    def test_comment_listing(self):
        self.assertEqual(f'{self.comment.name}', 'mamali')
        self.assertEqual(f'{self.comment.email}', 'mamal@gmail.com')
        self.assertEqual(f'{self.comment.subject}', 'Good Idea')
        self.assertEqual(f'{self.comment.message}', "You\'r blog is awsome.")
        