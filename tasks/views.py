from django.shortcuts import render, redirect
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

def add_task(request):
    if request.method == "POST":
        user = User.objects.last()
        title = request.POST.get('title')
        description = request.POST.get('description')
        is_completed = request.POST.get('is_completed') == 'on'

        # Create and save the Task object
        Task.objects.create(
            user=user,
            title=title,
            description=description,
            status=is_completed
        )
        return redirect('home')
    return render(request, 'add-task.html')
