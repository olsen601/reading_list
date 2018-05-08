from django.shortcuts import render, redirect, get_object_or_404

from ..forms import NewUserForm

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


def register(request):

    if request.method == 'POST':

        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            user = authenticate(username=request.POST['username'], password=request.POST['password1'])
            login(request, user)
            return redirect('reading:homepage')

        else:
            message = 'Please check the data you entered'
            return render(request, 'registration/register.html', { 'form' : form, 'message' : message } )

    else:
        form = NewUserForm()
        return render(request, 'registration/register.html', { 'form' : form } )

def profile(request, user_pk):
    user = User.objects.get(pk=user_pk)
    request_user = request.user

    return render(request, 'reading/users/profile.html', {'request_user' : request_user, 'user' : user } )
