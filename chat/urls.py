from django.urls import path
from . import views

urlpatterns = [
    path("chat_api/", views.chat_api, name="chat_api"),
]
