from django.contrib import admin
from .models import Post, Category, Blogger, Tag, Comment


admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Blogger)
admin.site.register(Comment)
