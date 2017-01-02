from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.utils.decorators import method_decorator
from .models import Task
from django.http import HttpResponseRedirect


class Manage(object):

    model = Task
    # @method_decorator(super_user)
    def dispatch(self, *args, **kwargs):
        # Make sure that superuser is logged in
        return super(Manage, self).dispatch(*args, **kwargs)


class TaskList(Manage, ListView):
    pass


class TaskAdd(Manage,  CreateView):
    fields = ['name']
    # template_name = 'manage/add.html'

    def get_success_url(self):
        return "/close/?msg=%s added successfully." %(self.kwargs['model'].capitalize())

class Active(Manage, DeleteView):

    # @method_decorator(super_user)
    def dispatch(self, *args, **kwargs):
        self.get_object().switch()
        return HttpResponseRedirect("/manage/list/" + self.kwargs['model'])
