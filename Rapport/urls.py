from django.urls import path
from . import views
urlpatterns = [
    path('create_Rapport/', views.create_Rapport, name='create_Rapport'),
    path('download/<str:pk>/', views.download_pdf, name='download_pdf'),
    path('open_pdf/<str:pk>/', views.open_pdf, name='open_pdf'),
    path('get_Rapport_by_id/<str:pk>/', views.get_Rapport_by_id, name='get_Rapport_by_id'),
    path('delete_Rapport/<str:pk>/', views.delete_Rapport, name='delete_Rapport'),
    path('update_Rapport/<str:pk>/', views.update_Rapport, name='update_Rapport'),
    path('get_Rapport_list/', views.get_Rapport_list, name='get_Rapport_list'),
    path('get_Rapport_list/<str:cin>/', views.get_Rapport_list_by_cin, name='get_Rapport_list_by_cin'),
    path('get_students_by_rapporteur_cin/<str:cin_president_jury>/', views.get_students_by_president_jury_cin, name='get_students_by_rapporteur_cin'),

]
