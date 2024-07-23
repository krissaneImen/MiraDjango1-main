# urls.py
from django import views
from django.urls import path
from .views import  Create_profile, update_profile , get_profile_by_cin , delete_profile

urlpatterns = [
     path('create/', Create_profile, name='Create_profile'),
     path('update/<str:cin>/', update_profile, name='update_profile'),
     path('profiles/cin/<str:cin>/', get_profile_by_cin, name='profile-by-cin'),
     path('delete_profile/<str:cin>/', delete_profile, name='delete_profile'),
    ]
