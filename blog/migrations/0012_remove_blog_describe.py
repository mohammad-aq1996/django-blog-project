# Generated by Django 4.0.2 on 2022-02-19 19:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_alter_blog_content'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='describe',
        ),
    ]
