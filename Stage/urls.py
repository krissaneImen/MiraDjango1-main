from django.urls import path
from . import views
urlpatterns = [
    path('create/', views.create_Stage, name='create_Stage'),
    path('update/<str:pk>/', views.update_Stage, name='update_Stage'),
    path('Remise_Rapport/', views.Remise_Rapport, name='Remise_Rapport'),
    path('update_Stage_DateJeri/', views.update_Stage_DateJeri, name='update_Stage_DateJeri'),
    path('delete/<str:pk>/', views.delete_Stage, name='delete_Tache'),
    path('get_Stage_by_id/<str:groupe_id>/', views.get_Stage_by_id, name='get_Stage_by_id'),
    path('etudiants_avec_stage/', views.get_etudiants_avec_stage, name='get_etudiants_avec_stage'),
    path('get_students_by_rapporteur_cin/<str:cin_president_jury>/', views.get_students_by_president_jury_cin, name='get_students_by_president_jury_cin'),
    path('mes_Stage/<str:cin>/', views.mes_Stage, name='mes_Stage'),
    path('get_all_Stage/', views.get_all_Stage, name='get_all_Stage'),
    path('update_fields/', views.update_fields, name='update_fields'),
    
    
]
