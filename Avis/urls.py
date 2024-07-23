from django.urls import path
from . import views
urlpatterns = [
    path('create/', views.create_Avis, name='create_Avis'),
    path('update/<str:groupe_id>/', views.update_avis, name='update_avis'),
    path('get_avis_by_id/<str:groupe_id>/', views.get_avis_by_id, name='get_avis_by_id'),
    path('get_all_avis/', views.get_all_avis, name='get_all_avis'),
    path('get_avis_by_group/<str:NomGroupe>/', views.get_avis_by_group, name='get_avis_by_group'),
    path('get_avis_by_state/<str:state>/', views.get_avis_by_state, name='get_avis_by_state'),
    path('get_avis_by_state_and_group/<str:state>/<str:group_id>/', views.get_avis_by_state_and_group, name='get_avis_by_state_and_group'),
    path('get_avis_by_cin/<str:cin>/', views.get_avis_by_cin, name='get_avis_by_cin'),
    
]