# Generated by Django 4.0.2 on 2022-02-18 14:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_rename_content_comment_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='blog',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blog.blog'),
        ),
    ]
