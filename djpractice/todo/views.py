from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Task
from django.http import HttpResponseRedirect


class Manage(object):

    model = Task
    fields = ['name', 'due_date', 'description', 'state', 'priority']
    success_url = "/"


class TaskList(Manage, ListView):
    pass


class TaskAdd(Manage,  CreateView):
    pass


class TaskUpdate(Manage, UpdateView):
    pass


class Active(Manage, DeleteView):

    # @method_decorator(super_user)
    def dispatch(self, *args, **kwargs):
        self.get_object().switch()
        return HttpResponseRedirect("/manage/list/" + self.kwargs['model'])
