from django.contrib import admin
from .models import Blog, Category, Blogger, Tag, Comment


admin.site.register(Blog)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Blogger)
admin.site.register(Comment)
