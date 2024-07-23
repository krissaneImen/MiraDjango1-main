from django.urls import path
from . import views
urlpatterns = [
    path('create_Attestation/', views.create_Attestation, name='create_Attestation'),
    path('update_Attestation/<str:demande_id>/', views.update_Attestation, name='update_Attestation'),
    path('get_attestation_by_id/<str:demande_id>/', views.get_attestation_by_id, name='get_attestation_by_id'),
    path('delete_attestation/<str:demande_id>/', views.delete_attestation, name='delete_attestation'),
    path('get_attestation_by_cin/<str:Cin>/', views.get_attestation_by_cin, name='get_attestation_by_cin'),
    
    
    ]
