from django.shortcuts import render
from .models import Cake, AboutSite
# Create your views here.


def home(request):
    cake_list = Cake.objects.all()
    context = {
        'cake_list':cake_list
    }
    return render(request, 'home.html', context)

def about(request):
    about_list = AboutSite.objects.all()
    context = {
        'about_list':about_list
    }
    return render(request, 'about.html', context)