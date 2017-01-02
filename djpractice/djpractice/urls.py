from django.conf.urls import url
from django.contrib import admin
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', TemplateView.as_view(template_name='index.html')),
    url(r'^css/bootstrap-cerulean.min.css$',
        lambda request: HttpResponseRedirect(
            '/static/charisma/css/bootstrap-cerulean.min.css')),
]
