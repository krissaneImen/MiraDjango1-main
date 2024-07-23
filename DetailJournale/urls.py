from django.urls import path
from . import views
urlpatterns = [
    path('create/', views.create_Journale, name='create_Journale'),
    path('update/<str:groupe_id>/', views.update_Journale, name='update_Journale'),
    path('update/<str:pk>/', views.update_Journale, name='update_Journale'),
    path('delete/<str:pk>/', views.delete_journale, name='delete_journale'),
    path('get_Journale_by_id/<str:groupe_id>/', views.get_Journale_by_id, name='get_Journale_by_id'),
    path('evaluer/<str:groupe_id>/', views.evaluer, name='evaluer'),
    path('get_all_journale/', views.get_all_journale, name='get_all_journale'),
    path('get_all_journale/<str:cin>/<str:id>/', views.mon_journale, name='mon_journale'),
    path('get_all_journale/<str:Cin>/', views.mes_journales, name='mes_journales'),
    path('export_all_data_xlsx/<str:detail_id>/', views.export_all_data_xlsx, name='export_all_data_xlsx'),
    path('get_students_by_rapporteur_cin/<str:cin_president_jury>/', views.get_students_by_president_jury_cin, name='get_students_by_president_jury_cin'),
    path('get_journales_by_cins/', views.get_journales_by_cins, name='get_journales_by_cins'),
    
]
