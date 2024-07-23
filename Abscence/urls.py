
from django.urls import path
from . import views
urlpatterns = [
    path('my_IpAdress/', views.my_view, name='my_view'),
    path('create/', views.create_groupe, name='create_groupe'),
    path('export_fiche_presence/<str:fiche_id>/', views.export_fiche_presence_xlsx, name='export_fiche_presence_xlsx'),
    path('export_fiche_presence_pdf/<str:fiche_id>/', views.export_fiche_presence_pdf, name='export_fiche_presence_pdf'),
    path('update/<str:groupe_id>/', views.update_groupe, name='update_groupe'),
    path('get_groupe_by_id/<str:groupe_id>/', views.get_groupe_by_id, name='get_groupe_by_id'),
    path('check_ip_allowed/<str:ip_address>/', views.check_ip_allowed, name='check_ip_allowed'),
    path('allow_update/<str:idFiche>/', views.allow_update, name='allow_update'),
    path('delete_groupe/<str:groupe_id>/', views.delete_groupe, name='delete_groupe'),
    path('get_all_groupes/', views.get_all_groupes, name='get_all_groupes'),
    path('get_classe_by_cin/<str:cin>/', views.get_classe_by_cin, name='get_classe_by_cin'),
    path('get_groupes_by_cinenseignant/<str:cinenseignant>/', views.get_groupes_by_cinenseignant, name='get_groupes_by_cinenseignant'),
    
]
