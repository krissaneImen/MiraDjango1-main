from django.urls import path
from . import views
urlpatterns = [
    path('create/', views.create_Tache, name='create_Tache'),
    path('nombre_taches_par_journale/<str:id>/', views.nombre_taches_par_journale, name='nombre_taches_par_journale'),
    path('update/<str:pk>/', views.update_Tache, name='update_Tache'),
    path('delete/<str:pk>/', views.delete_Tache, name='delete_Tache'),
    path('get_Tache_by_id/<str:groupe_id>/', views.get_Tache_by_id, name='get_Tache_by_id'),
    path('get_all_tache/<str:id>/', views.get_all_tache, name='get_all_tache'),
     
]
