from django.shortcuts import render

def homepage(request):
    return render(request, 'reading/home.html')
