from django.urls import path, include
from rest_framework import routers
from . import views
app_name = 'api'
router = routers.SimpleRouter()
router.register('post', views.PostViewSet)
urlpatterns = [
    path('', include(router.urls)),
]
