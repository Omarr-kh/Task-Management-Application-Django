from django.contrib import admin
from .models import Task

# register Task model to the admin panel
admin.site.register(Task)
