from django.urls import path
from . import views

urlpatterns = [
    path('', views.work_index, name='work_index'),
    path('<int:project_id>/', views.work_detail, name='work_detail'),
    path('create/', views.create_work, name='create_work'),
]