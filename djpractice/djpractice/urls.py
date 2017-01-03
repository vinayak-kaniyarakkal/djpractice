from django.conf.urls import url
from django.contrib import admin
from todo.views import TaskList, TaskAdd, TaskUpdate
from django.http import HttpResponseRedirect


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', TaskList.as_view()),
    url(r'^add/$', TaskAdd.as_view()),
    url(r'^edit/(?P<pk>\d+)/$', TaskUpdate.as_view()),
    url(r'.*css/bootstrap-cerulean.min.css$',
        lambda request: HttpResponseRedirect(
            '/static/charisma/css/bootstrap-cerulean.min.css')),
]
