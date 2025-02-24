from django.shortcuts import render


def home(request):
    """
    Home page view function 
    """
    return render(request, 'home/index.html')