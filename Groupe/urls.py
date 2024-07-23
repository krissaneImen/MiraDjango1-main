from django.urls import path
from . import views
urlpatterns = [
    path('create/', views.create_groupe, name='create_groupe'),
    path('update/<str:groupe_id>/', views.update_groupe, name='update_groupe'),
    path('get_groupe_by_id/<str:groupe_id>/', views.get_groupe_by_id, name='get_groupe_by_id'),
    path('delete_groupe/<str:groupe_id>/', views.delete_groupe, name='delete_groupe'),
    path('get_students_by_group/<str:groupe_id>/', views.get_students_by_group, name='get_students_by_group'),
    path('get_all_groupes/', views.get_all_groupes, name='get_all_groupes'),
    path('Groupe_list/', views.Groupe_list, name='Groupe_list'),
    path('get_classe_by_cin/<str:cin>/', views.get_classe_by_cin, name='get_classe_by_cin'),
    
]
