from django.db import models


class Comment(models.Model):
    # creating a table for comments in database
    name = models.CharField(max_length=150, verbose_name='نام')
    email = models.EmailField(verbose_name='ایمیل')
    subject = models.CharField(max_length=250, verbose_name='موضوع')
    message = models.TextField(verbose_name='پیام')
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True, verbose_name='زمان')

    class Meta:
        verbose_name = 'نظر'
        verbose_name_plural = 'نظرات صفحه تماس با ما'

    def __str__(self):
        return self.email

