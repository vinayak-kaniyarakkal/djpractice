from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView
from .models import Task


class Manage(object):

    model = Task
    fields = ['name', 'due_date', 'description', 'state', 'priority']
    success_url = '/'


class TaskList(Manage, ListView):
    pass


class TaskAdd(Manage,  CreateView):
    pass


class TaskUpdate(Manage, UpdateView):
    pass
