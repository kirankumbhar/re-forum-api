from  django.urls import path, include

from rest_framework import routers

from.views import MeAPIView, PostViewSet, CommentViewSet, UserViewSet, UserRegisterView

router = routers.DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'users', UserViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('me', MeAPIView.as_view(), name="meapi"),
    path('register/', UserRegisterView.as_view(), name='register')
]