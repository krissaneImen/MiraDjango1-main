from django.urls import path
from . import views
urlpatterns = [
    path('create/', views.create_emploi, name='create_emploi'),
    path('update/<str:groupe_id>/', views.update_emploi, name='update_emploi'),
    path('get_emploi_by_id/<str:groupe_id>/', views.get_emploi_by_id, name='get_emploi_by_id'),
    path('delete_emploi/<str:groupe_id>/', views.delete_emploi, name='delete_emploi'),
    path('get_seance_par_horaire_jourSemaine/<str:horaire>/<str:jourSemaine>/', views.get_seance_par_horaire_jourSemaine, name='get_seance_par_horaire_jourSemaine'),
    path('get_all_seances/', views.get_all_seances, name='get_all_seances'),
    path('get_emploi_by_cin/<str:cin>/', views.get_emploi_by_cin, name='get_emploi_by_cin'),
    path('get_seances_by_cin/<str:cin>/', views.get_seances_by_cin, name='get_seances_by_cin'),
    
]
