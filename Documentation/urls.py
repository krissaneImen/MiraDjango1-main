from django.urls import path
from . import views
urlpatterns = [
    path('add_rule/', views.add_rule, name='add_rule'),
    path('update/<str:identifiant>/', views.update_reglement, name='update_reglement'),
    path('reglement_by_id/<str:identifiant>/', views.reglement_by_id, name='reglement_by_id'),
    path('delete_reglement/<str:identifiant>/', views.delete_reglement, name='delete_reglement'),
    path('reglement_interieur/', views.reglement_interieur, name='reglement_interieur'),
    path('reglement_examens/', views.reglement_examens, name='reglement_examens'),
    path('reglements/', views.reglements, name='reglements'),
    path('reglements/usertype/<str:userType>/', views.reglements_by_usertype, name='reglements_by_usertype'),
    path('reglements/<str:reglement_type>/', views.reglement_by_type, name='reglement_by_type'),
]
