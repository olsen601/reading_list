from django.urls import path
from .views import views, views_users, views_genres, views_lists, views_books, views_searches

from django.contrib.auth import views as auth_views


app_name = 'reading'

urlpatterns = [

    path('', views.homepage, name='homepage'),

    #Genres
    path('user/<int:user_pk>/genres/', views_genres.genres_for_user, name='genres_for_user'),

    #Genre list

    #Book

    #Search

    #User Profile
    path('user/profile/', views_users.profile, name='profile'),
    path('user/profile/<int:user_pk>/', views_users.profile, name='user_profile'),

]
