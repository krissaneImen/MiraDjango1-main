from django.urls import path
from . import views
urlpatterns = [
    path('create_type/', views.create_type, name='create_type'),
    path('get_type_by_id/<str:pk>/', views.get_type_by_id, name='get_type_by_id'),
    path('get_all_type/<str:userType>/', views.get_all_type, name='get_all_type'),
    path('delete_type/<str:pk>/', views.delete_type, name='delete_type'),
    path('update_type/<str:pk>/', views.update_type, name='update_type'),
    path('get_all_type/', views.get_all_type, name='get_all_type'),
    path('get_type_list/', views.get_type_list, name='get_type_list'),
    path('types/<str:userType>/<str:fonctionalite>/', views.get_types_by_user_type_and_functionality, name='get_types_by_user_type_and_functionality'),
    ]
