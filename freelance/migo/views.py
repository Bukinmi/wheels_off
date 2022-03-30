from django.shortcuts import render
from django.http import HttpResponse
from .models import Meetups

# Create your views here.

def index(request):
    meetups = Meetups.objects.all()
    return render (request, 'index.html', {
        'meetups': meetups
    })
