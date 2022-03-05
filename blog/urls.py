from django.urls import path
from .views import (PostListView, SearchView, PostCategory,
                    PostTag, post_detail_view, login_view,
                    logout_view, PostCreateView, PostUpdateView,
                    PostDeleteView, PostDraftListView)


app_name = 'blog'
urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('search/', SearchView.as_view(), name='search'),
    path('category/<slug:category>/', PostCategory.as_view(), name='category_view'),
    path('tags/<slug:tag>/', PostTag.as_view(), name='tag_view'),
    path('blogs/<int:pk>/', post_detail_view, name='post_detail'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('create/', PostCreateView.as_view(), name='post_create'),
    path('update/<int:pk>/', PostUpdateView.as_view(), name='post_update'),
    path('delete/<int:pk>/', PostDeleteView.as_view(), name='post_delete'),
    path('draft/', PostDraftListView.as_view(), name='post_draft'),

]
