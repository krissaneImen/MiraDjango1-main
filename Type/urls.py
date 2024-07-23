from django.urls import path
from . import views
urlpatterns = [
    path('add_Type/', views.add_Type, name='add_Type'),
    path('update/<str:name>/', views.update_type, name='update_reglement'),
    path('type_by_id/<str:name>/', views.reglement_by_id, name='reglement_by_id'),
    path('delete_type/<str:name>/', views.delete_reglement, name='delete_reglement'),
    path('types/', views.types, name='types'),
]
