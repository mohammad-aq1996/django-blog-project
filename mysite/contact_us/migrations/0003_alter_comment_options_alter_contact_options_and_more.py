# Generated by Django 4.0.3 on 2022-04-09 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact_us', '0002_rename_title_comment_subject'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'verbose_name': 'نظر', 'verbose_name_plural': 'نظرات صفحه تماس با ما'},
        ),
        migrations.AlterModelOptions(
            name='contact',
            options={'verbose_name': 'اطلاعات صفحه تماس با ما', 'verbose_name_plural': 'اطلاعات صفحه تماس با ما'},
        ),
        migrations.AlterField(
            model_name='comment',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='زمان'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='ایمیل'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='message',
            field=models.TextField(verbose_name='پیام'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='name',
            field=models.CharField(max_length=150, verbose_name='نام'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='subject',
            field=models.CharField(max_length=250, verbose_name='موضوع'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='address',
            field=models.CharField(max_length=400, verbose_name='آدرس'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='describe',
            field=models.CharField(max_length=200, verbose_name='توضیحات'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='ایمیل'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='phone_no',
            field=models.CharField(max_length=11, verbose_name='شماره تماس'),
        ),
    ]