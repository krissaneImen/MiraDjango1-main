from django.urls import path
from . import views
urlpatterns = [
    path('create_Calendrier/', views.create_Calendrier, name='create_Calendrier'),
    path('download/<str:pk>/', views.download_pdf, name='download_pdf'),
    path('open_pdf/<str:pk>/', views.open_pdf, name='open_pdf'),
    path('get_Calendrier_by_id/<str:pk>/', views.get_Calendrier_by_id, name='get_Calendrier_by_id'),
    path('delete_Calendrier/<str:pk>/', views.delete_Calendrier, name='delete_Calendrier'),
    path('update_Calendrier/<str:pk>/', views.update_Calendrier, name='update_Calendrier'),
    path('get_Calandrier_list/', views.get_Calandrier_list, name='get_Calandrier_list'),
    ]
