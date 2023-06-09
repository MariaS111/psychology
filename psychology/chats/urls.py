from django.urls import path
from .views import chat_list, chat_view, create_chat

urlpatterns = [
    path('', chat_list, name='list_of_chats'),
    path('<int:pk>/', chat_view, name='chat'),
    path('create/', create_chat, name='create_chat'),
]