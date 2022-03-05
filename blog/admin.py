from django.contrib import admin
from .models import Post, Category, Blogger, Tag, Comment

admin.site.register(Blogger)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'created_at']
    list_filter = ['created_at']
    search_fields = ['title', 'content']
    raw_id_fields = ('author',)
    # list_editable = ['status']
    # prepopulated_fields = {'slug': ['title']}


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
    list_display_links = ['slug']


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
    list_display_links = ['slug']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['title', 'post', 'status']
    list_editable = ['status']




