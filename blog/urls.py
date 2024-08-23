# blog/urls.py
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import  views

router = DefaultRouter()
router.register(r'posts', views.PostViewsets)
router.register(r'comments', views.CommentViewSet)
router.register(r'users', views.UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
