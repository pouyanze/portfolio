from django.urls import path
from . import views

urlpatterns = [
    path('', views.ContactView.as_view(), name='contact'),
    path('messages/', views.MessageListView.as_view(), name='view_messages'),
    path('messages/<int:pk>/delete/', views.MessageDeleteView.as_view(), name='message_delete'),
]