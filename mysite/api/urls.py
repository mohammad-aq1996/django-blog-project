from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt import views as jwt_views

from . import views


app_name = 'api'

router = routers.SimpleRouter()
router.register('post', views.PostViewSet)
router.register('tag', views.TagViewSet)
router.register('category', views.CategoryViewSet)
router.register('comment', views.CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),

    path('token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]
