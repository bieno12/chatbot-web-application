from django.urls import path
from . import views
from django.conf import settings

urlpatterns = [
    path('', views.home, name="home"),
    path('conversations/', views.conversations, name="conversations"),
    path('conversations/<int:id>', views.conversation, name="del_conversation"),
    path('conversations/<int:conv_id>/messages', views.messages, name="messages"),
]