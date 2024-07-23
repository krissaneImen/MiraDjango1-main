from django.urls import path
from . import views
urlpatterns = [
    path('create_Support/', views.create_Support, name='create_Support'),
    path('chat/', views.chat, name='chat'),
    path('getResume/<str:pk>/', views.getResume, name='getResume'),
    path('download/<str:pk>/', views.download_pdf, name='download_pdf'),
    path('extract_pdf_data/<str:pk>/', views.extract_pdf_data, name='extract_pdf_data'),
    path('open_pdf/<str:pk>/', views.open_pdf, name='open_pdf'),
    path('get_Support_by_id/<str:pk>/', views.get_Support_by_id, name='get_Support_by_id'),
    path('delete_support/<str:pk>/', views.delete_support, name='delete_support'),
    path('update_support/<str:pk>/', views.update_support, name='update_support'),
    path('get_support_list/', views.get_support_list, name='get_support_list'),
    
    
    ]
