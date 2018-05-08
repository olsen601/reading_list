from django.shortcuts import render, redirect, get_object_or_404

from ..models import Categorie, Genre, GenreList

from django.contrib.auth.models import User

def genres_for_user(request, user_pk):

    user_pk = User.objects.get(pk=user_pk)

    genres = Genre.objects.filter(user=user_pk).order_by('name').reverse()


    return render(request, 'reading/genres/genre/genres.html', {'genres':genres})
