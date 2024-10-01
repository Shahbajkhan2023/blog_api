from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('profile/update/', views.ProfileUpdateView.as_view(), name='profile_update'),
    path('create/', views.PostCreateView.as_view(), name='post_create'),
]
