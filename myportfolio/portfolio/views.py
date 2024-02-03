from django.shortcuts import render

# Create your views here.
# portfolio/views.py
from .models import Project

def index(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/index.html', {'projects': projects})
