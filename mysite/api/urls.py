from django.urls import path, include
from rest_framework import routers
from . import views


app_name = 'api'

router = routers.SimpleRouter()
router.register('post', views.PostViewSet)
router.register('tag', views.TagViewSet)
router.register('category', views.CategoryViewSet)
router.register('comment', views.CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
