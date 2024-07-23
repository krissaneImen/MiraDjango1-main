# urls.py
from django.urls import path
from . import views
urlpatterns = [
    path('create/', views.create_reglement, name='create_reglement'),
    path('open_pdf/<str:pk>/', views.open_pdf, name='open_pdf'),
    path('update_reglement/<str:pk>/', views.update_reglement, name='update_reglement'),
    path('get_Reglement_by_id/<str:pk>/', views.get_Reglement_by_id, name='get_Reglement_by_id'),
    path('delete_reglement/<str:pk>/', views.delete_reglement, name='delete_reglement'),
    path('download_pdf/<str:pk>/', views.download_pdf, name='download_pdf'),
    path('get_reglement_list/<str:reglement_type>/', views.get_reglement_by_type, name='get_reglement_by_type'),
    path('get_reglement_list/', views.get_reglement_list, name='get_reglement_list'),
  ]
