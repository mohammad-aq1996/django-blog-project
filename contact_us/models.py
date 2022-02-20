from django.db import models


class Contact(models.Model):
    address = models.CharField(max_length=400)
    phone_no = models.CharField(max_length=11)
    email = models.EmailField()
    describe = models.CharField(max_length=200)

    def __str__(self):
        return self.email


class Comment(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    subject = models.CharField(max_length=250)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.email

