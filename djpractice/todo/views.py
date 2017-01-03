from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView
from .models import Task


class Manage(object):

    model = Task
    fields = ['name', 'due_date', 'description', 'state', 'priority']
    success_url = '/'

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(Manage, self).form_valid(form)


class TaskList(Manage, ListView):

    def get_queryset(self):
        qs = super(Manage, self).get_queryset()
        if self.request.GET.get('start'):
            qs = qs.filter(due_date__gte=self.request.GET.get('start'))
        if self.request.GET.get('end'):
            qs = qs.filter(due_date__lte=self.request.GET.get('end'))
        return qs.filter(owner=self.request.user)

    def get_context_data(self):
        context = super(TaskList, self).get_context_data()
        context['start'] = self.request.GET.get('start')
        context['end'] = self.request.GET.get('end')
        return context


class TaskAdd(Manage,  CreateView):
    pass


class TaskUpdate(Manage, UpdateView):
    pass
