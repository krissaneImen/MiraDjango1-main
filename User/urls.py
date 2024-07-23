from django.urls import path
from .views import user_registration, user_login  ,check_email , check_identifient

from . import views
urlpatterns = [
    path('register/', user_registration, name='user-registration'),
    path('login/', user_login, name='user-login'),
    path('check_identifient/<str:cin>/', views.check_identifient, name='check_identifient'),
    path('inactive_users/', views.inactive_users, name='inactive_users'),
    path('active_users/', views.active_users, name='active_users'),
    path('validate_user_account/<str:cin>/', views.validate_user_account, name='validate_user_account'),
    path('distribuer_titre/<str:cin>/<str:titre>', views.distribuer_titre, name='distribuer_titre'),
    path('deactive_user_account/<str:cin>/', views.deactive_user_account, name='deactive_user_account'),
    path('check_email/', views.check_email, name='check_email'),
    path('send_Email/', views.send_Email, name='send_Email'),
    path('send_test_code/', views.send_test_code, name='send_test_code'),
    path('check_cin/', views.check_cin, name='check_cin'),
    path('start-session/', views.start_session, name='start_session'),
    path('check-session/', views.check_session, name='check_session'),
    path('end-session/', views.end_session, name='end_session'),
    path('send_verification_code/', views.send_verification_code, name='send_verification_code'),
    #reset password
    path('user_detail/<str:cin>/', views.user_detail, name='user_detail'),
    path('get_email_by_cin/<str:cin>/', views.get_email_by_cin, name='get_email_by_cin'),
    path('fetch_user_type/<str:cin>/', views.fetch_user_type, name='fetch_user_type'),
    path('demande_reset_password/<str:cin>/', views.demande_reset_password, name='demande_reset_password'),
    path('reset_password_users/', views.reset_password_users, name='reset_password_users'),
    path('reset_password/', views.reset_password, name='reset_password'),
    path('delete_user/<str:cin>/', views.delete_user, name='delete_user'),
    path('enseignants_list/', views.enseignants_list, name='enseignants_list'),
    path('etudiant_list/', views.etudiant_list, name='etudiant_list'),
]
