from django.urls import path
from . import views


urlpatterns = [
    path('', views.work_index, name='work_index'),
    path('<int:pk>/', views.work_detail, name='work_detail'),
    path('create/', views.create_work, name='create_work'),
    path('<int:pk>/edit/', views.EditWork.as_view(), name='edit_work'),
    path('<int:pk>/delete/', views.DeleteWork.as_view(), name='delete_work'),
]