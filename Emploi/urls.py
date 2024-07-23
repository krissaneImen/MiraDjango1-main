from django.urls import path
from . import views
urlpatterns = [
    path('class_schedule/', views.upload_file, name='class_schedule'),
    path('download/<str:pk>/', views.download_pdf, name='download_pdf'),
    path('open_pdf/<str:pk>/', views.open_pdf, name='open_pdf'),
    path('get_employment_by_id/<str:pk>/', views.get_employment_by_id, name='get_employment_by_id'),
    path('get_employment_list/<str:emploi_type>/', views.get_employment_by_type, name='get_employment_by_type'),
    path('delete_employment/<str:pk>/', views.delete_employment, name='delete_employment'),
    path('update_employment/<str:pk>/', views.update_employment, name='update_employment'),
    path('get_employment_list/', views.get_employment_list, name='get_employment_list'),
   
]
