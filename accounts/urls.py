from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, signup, login, token_back


router=DefaultRouter()
router.register('User',UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('signup/', signup),
    path('login/', login),
    path('token_back/', token_back),
]