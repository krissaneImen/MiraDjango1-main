# urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.upload_file, name='upload_file'),  # URL for file upload
    path('open_pdf/<str:pk>/', views.open_pdf, name='open_pdf'),
    path('download/<str:file_id>/', views.download_file, name='download_file'),  # URL for file download
    path('get_file/<str:file_id>/', views.get_file, name='get_file'),  # URL for file download
]
