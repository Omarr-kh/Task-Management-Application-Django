from django.shortcuts import render
from django.http import HttpResponse
from .models import Task
from django.contrib.auth.models import User

# Create your views here.
def home(request):
    user = User.objects.last()
    tasks = Task.objects.filter(user=user)
    context = {
        "tasks": tasks
    }
    return render(request, 'home.html', context)
