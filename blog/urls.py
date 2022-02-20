from django.urls import path
from .views import BlogListView, SearchView, BlogCategory, BlogTag, blog_detail_view


app_name = 'blog'
urlpatterns = [
    path('', BlogListView.as_view(), name='blog_list'),
    path('search/', SearchView.as_view(), name='search'),
    path('category/<slug:slug>/', BlogCategory.as_view(), name='category_view'),
    path('tags/<slug:tag>/', BlogTag.as_view(), name='blog_tag'),
    path('blogs/<int:pk>/', blog_detail_view, name='detail')
]
