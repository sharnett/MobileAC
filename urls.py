from django.conf.urls.defaults import patterns, include, url
from django.views.generic import UpdateView, ListView
from mobileAC.models import AC, ThermoReading
from mobileAC.forms import ACUpdateForm
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', ListView.as_view(model=ThermoReading, context_object_name='reading_list')),
    (r'^(?P<pk>\d+)/$', UpdateView.as_view(model=AC, form_class=ACUpdateForm, success_url="/1")),
    url(r'^admin/', include(admin.site.urls)),
)
