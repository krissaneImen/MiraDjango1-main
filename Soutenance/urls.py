from django.urls import path
from . import views

urlpatterns = [
   
    path('create/', views.create_soutenance, name='create_soutenance'),
    path('update/<str:groupe_id>/', views.update_soutenance, name='update_soutenance'),
    path('soutenance/<str:groupe_id>/', views.get_soutenance_by_id, name='get_soutenance_by_id'),
    path('soutenances/', views.get_all_soutenances, name='get_all_soutenances'),
    path('delete/<str:groupe_id>/', views.delete_soutenance, name='delete_soutenance'),
    path('list/', views.soutenance_list, name='soutenance_list'),
    path('encadrant/<str:cin_encadreur>/', views.get_students_by_encadrant_cin, name='get_students_by_encadrant_cin'),
    path('presidentjury/<str:cin_president_jury>/', views.get_students_by_president_jury_cin, name='get_students_by_president_jury_cin'),
    path('rapporteur/<str:cin_rapporteur>/', views.get_students_by_rapporteur_cin, name='get_students_by_rapporteur_cin'),

]
