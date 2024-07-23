from django.urls import path
from . import views

urlpatterns = [
    path('create/<str:cin>/', views.create_conversation, name='create_conversation'),
    path('chat/', views.chat, name='chat'),
    path('conversation/<str:conversation_id>/add_message/', views.add_message, name='add_message'),
    path('update/<str:idConversation>/', views.update_conversation, name='update_conversation'),
    path('get_conversation_by_id/<str:idConversation>/', views.get_conversation_by_id, name='get_conversation_by_id'),
    path('get_all_conversation/<str:cin>/', views.get_all_conversation, name='get_all_conversation'),
    path('delete_Conversation/<str:idConversation>/', views.delete_Conversation, name='delete_Conversation'),
    path('get_Message_by_conversation/<str:idConversation>/', views.get_Message_by_conversation, name='get_Message_by_conversation'),

]

