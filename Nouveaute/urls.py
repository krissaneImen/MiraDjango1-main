from django.urls import path
from . import views
urlpatterns = [
    path('create/', views.create_nouveaute, name='create_nouveaute'),
    path('nouveaute/<str:Identifiant>/', views.retrieve_nouveaute, name='retrieve_nouveaute'),
    path('update/<str:Identifiant>/', views.update_nouveaute, name='update_nouveaute'),
    path('delete/<str:Identifiant>/', views.delete_nouveaute, name='delete_nouveaute'),
    path('list/', views.list_nouveautes, name='list_nouveautes'),
]
