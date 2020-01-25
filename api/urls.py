from  django.urls import path, include

from rest_framework import routers

from.views import PostViewSet, CommentViewSet, UserViewSet, UserRegisterView

router = routers.DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'users', UserViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('register/', UserRegisterView.as_view(), name='register')
]