from django.urls import path
from . import views
urlpatterns = [
    path('create/', views.create_Evaluation, name='create_Evaluation'),
    path('update/<str:groupe_id>/', views.update_Evaluation, name='update_Evaluation'),
    path('delete/<str:pk>/', views.delete_Evaluation, name='delete_Evaluation'),
    path('get_Evaluation_by_id/<str:groupe_id>/', views.get_Evaluation_by_id, name='get_Evaluation_by_id'),
    path('get_Evaluation/<str:id>/', views.get_Evaluation, name='get_Evaluation'),
    path('get_all_Evaluations/', views.get_all_Evaluations, name='get_all_Evaluations'),
    path('get_all_Evaluations/<str:cin>/<str:id>/', views.get_Evaluation, name='get_Evaluation'),
    path('get_all_Evaluations/<str:cin>/', views.mes_Evaluation, name='mes_Evaluation'),
    
]
