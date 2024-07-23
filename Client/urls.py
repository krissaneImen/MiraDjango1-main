from django.urls import path
from . import views
urlpatterns = [
    path('create/', views.create_Institut, name='create_Institut'),
    path('update/<str:institut_id>/', views.update_institut, name='update_institut'),
    path('get_Institut/', views.get_Institut, name='get_Institut'),
    
]
