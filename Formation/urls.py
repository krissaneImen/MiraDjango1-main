# urls.py
from django import views
from django.urls import path

from Formation.views import Create_Formation,delete_formation,get_formations, get_formations_by_date, get_all_formations, get_formation_by_cin, update_formation

urlpatterns = [
     path('create/', Create_Formation, name='Create_Formation'),
     path('update/<str:Identifiant>/', update_formation, name='update_formation'),
     path('getFormation/<str:Identifiant>/', get_formation_by_cin, name='get_formation_by_cin'),
     path('delete_formation/<str:Identifiant>/', delete_formation, name='delete_formation'),
     path('formations/<str:userType>/', get_all_formations, name='get_all_formations'),
     path('formations/', get_formations, name='get_formations'),
     path('formations/<str:userType>/<str:date_min>/<str:date_max>/', get_formations_by_date, name='get_formations_by_date'),
    ] 
