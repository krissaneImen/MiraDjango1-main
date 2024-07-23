# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('pdffiles/', views.pdf_file_list, name='pdf_file_list'),
    path('pdffiles/<str:pk>/', views.pdf_file_detail, name='pdf_file_detail'),
    path('files/', views.file_list_view, name='file_list'),
    path('files/<str:name>/download/', views.download_file_view, name='download_file'),
    path('create/', views.pdf_file_create, name='pdf_file_create'),
    path('get_all_files/', views.get_all_files, name='get_all_files'),
]
