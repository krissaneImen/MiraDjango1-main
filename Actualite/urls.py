from django.urls import path
from . import views
urlpatterns = [
    path('create_actualite/', views.create_actualite, name='create_actualite'),
    path('download/<str:pk>/', views.download_pdf, name='download_pdf'),
    path('open_pdf/<str:pk>/', views.open_pdf, name='open_pdf'),
    path('get_actualite_by_id/<str:pk>/', views.get_actualite_by_id, name='get_actualite_by_id'),
    path('get_all_actualite/<str:userType>/', views.get_all_actualite, name='get_all_actualite'),
    path('delete_actualite/<str:pk>/', views.delete_actualite, name='delete_actualite'),
    path('update_actualite/<str:pk>/', views.update_actualite, name='update_actualite'),
    path('get_actualite_list/', views.get_actualite_list, name='get_actualite_list'),
    
    
    ]
