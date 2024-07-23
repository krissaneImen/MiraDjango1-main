from django.urls import path
from . import views
urlpatterns = [
    path('create_photocopie/', views.create_photocopie, name='create_photocopie'),
    path('download/<str:pk>/', views.download_pdf, name='download_pdf'),
    path('open_pdf/<str:pk>/', views.open_pdf, name='open_pdf'),
    path('get_photocopie_by_id/<str:pk>/', views.get_photocopie_by_id, name='get_photocopie_by_id'),
    path('get_photocopie_by_Demande/<str:idDemande>/', views.get_photocopie_by_Demande, name='get_photocopie_by_Demande'),
    path('delete_photocopie/<str:pk>/', views.delete_photocopie, name='delete_photocopie'),
    path('update_photocopie/<str:pk>/', views.update_photocopie, name='update_photocopie'),
    path('get_photocopie_list/', views.get_photocopie_list, name='get_photocopie_list'),
    path('photocopie_by_cin/<str:cin>/', views.get_photocopie_list_by_cin, name='get_photocopie_list_by_cin'),
]
