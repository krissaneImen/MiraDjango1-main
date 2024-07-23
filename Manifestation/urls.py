from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_manifestation, name='create_manifestation'),
    path('update/<str:Identifiant>/', views.update_manifestation, name='update_manifestation'),
    path('getManifestation/<str:Identifiant>/', views.get_manifestation_by_id, name='get_manifestation_by_id'),
    path('delete_manifestation/<str:Identifiant>/', views.delete_manifestation, name='delete_manifestation'),
    path('manifestations/<str:userType>/', views.get_all_manifestations_by_userType, name='get_all_manifestations_by_userType'),
    path('manifestations/<str:userType>/<str:date_min>/<str:date_max>/', views.get_manifestations_by_date, name='get_manifestations_by_date'),
   
]
