from django.urls import path
from . import views


urlpatterns = [
    path('', views.blog_index, name='blog_index'),
    path('<int:pk>/', views.post_detail, name='post_detail'),
    path('create/', views.create_post, name='create_post'),
    path('<int:pk>/edit/', views.EditPost.as_view(), name='edit_post'),
    path('<int:pk>/delete/', views.DeletePost.as_view(), name='delete_post'),
    path('posts/<int:pk>/favorite/', views.favorite_post, name='favorite_post'),
    path('favorite-posts/', views.favorite_posts, name='favorite_posts'),
    path('remove-favorite/<int:pk>/', views.remove_favorite, name='remove_favorite'),
]