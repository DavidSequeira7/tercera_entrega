from django.urls import path
from . import views

app_name = 'AppPeliculas'

urlpatterns = [
    path('movies/', views.movie_list),
    path('movies/<int:pk>/', views.movie_detail),
    path('actors/', views.actor_list),
    path('actors/<int:pk>/', views.actor_detail),
    path('reviews/', views.review_list),
    path('reviews/<int:pk>/', views.review_detail),
    path('addmovie/', views.add_movies),
    path('search/',views.search),
    path('res/',views.search_res),
]