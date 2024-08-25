from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Task
from django.contrib.auth.models import User
from django.core.paginator import Paginator

# Create your views here.


def home(request):
    """ View to show all tasks using pagination (5 per page) """

    user = User.objects.last()
    tasks = Task.objects.filter(user=user)

    # pagination with maximum of 5 tasks per page
    paginator = Paginator(tasks, 5)

    # Get the page number from the query string
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        "tasks": page_obj
    }

    # render a certain page
    return render(request, 'home.html', context)


def add_task(request):
    """ View to add a new task to the database """

    if request.method == "POST":
        user = User.objects.last()

        # retrieve task fields from the form inputs
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


def view_task(request, task_id):
    """ View to show a specific task based on it's id """

    task = Task.objects.get(id=task_id)
    context = {
        "task": task
    }
    return render(request, 'view-task.html', context)


def update_task(request, task_id):
    """ View to update a specific task based on it's id """

    task = Task.objects.get(id=task_id)
    context = {
        "task": task
    }

    if request.method == "POST":
        # update the task fields from the form inputs and save it
        task.title = request.POST.get('title')
        task.description = request.POST.get('description')
        task.status = request.POST.get('is_completed') == 'on'
        task.save()

        return redirect(reverse('view-task', args=[task.id]))
    return render(request, 'update-task.html', context)


def delete_task(request, task_id):
    """ View to delete a specific task based on it's id """

    task = Task.objects.get(id=task_id)
    task.delete()

    current_page = request.GET.get('page', 1)

    # Redirect back to the same page
    return redirect(f'/tasks?page={current_page}')
