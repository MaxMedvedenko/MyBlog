from django.urls import path
from . import views

urlpatterns = [
    # Маршрут для списку постів
    path('', views.post_list, name='post_list'),

    # Маршрут для детальної сторінки посту
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),

    # Маршрут для списку постів за автором
    path('author/<int:author_id>/', views.posts_by_author, name='posts_by_author'),
]