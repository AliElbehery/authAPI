from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, signup, login


router=DefaultRouter()
router.register('User',UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('signup/', signup),
    path('login/', login),
]