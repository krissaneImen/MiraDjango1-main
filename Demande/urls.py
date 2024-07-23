# urls.py
from django import views
from django.urls import path

from .views import create_demande,get_demande_by_cin, update_demande_etat, update_demande,get_demande_by_id, delete_demande , get_demande_by_responsable

urlpatterns = [
     path('create/', create_demande, name='Create_Formation'),
     path('update/<str:demande_id>/', update_demande, name='update_demande'),
     path('get_demande_by_cin/<str:Cin>/', get_demande_by_cin, name='get_demande_by_cin'),
     path('get_demande_by_id/<str:demande_id>/', get_demande_by_id, name='get_demande_by_id'),
     path('demandes/<str:Cin>/', get_demande_by_cin, name='get_demande_by_cin'),
     path('delete_demande/<str:demande_id>/', delete_demande, name='delete_demande'),
     path('demandes/responsable/<str:responsable_name>/', get_demande_by_responsable, name='get_demande_by_responsable'),
     path('update_demande_etat/<str:demande_id>/<str:etat>/', update_demande_etat, name='update_demande_etat'),
    
    ] 
