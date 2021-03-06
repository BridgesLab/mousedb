"""This urlconf sets the directions for the timed_mating app.

It takes a url in the form of /plug/something and sends it to the appropriate view class or function."""

from django.conf.urls import url

from mousedb.timed_mating import views

urlpatterns = [
    url(r'^$', views.PlugEventsList.as_view(), name="plugevents-list"),
    url(r'^(?P<pk>\d+)/?$', views.PlugEventsDetail.as_view(), name="plugevents-detail"),
    url(r'^new/?$', views.PlugEventsCreate.as_view(), name="plugevents-new"),
    url(r'^(?P<pk>\d+)/edit/?$', views.PlugEventsUpdate.as_view(), name="plugevents-edit"),
    url(r'^(?P<pk>\d+)/delete/?$', views.PlugEventsDelete.as_view(), name="plugevents-delete"),
    url(r'^breeding/(?P<breeding_id>\d*)/new/?$', views.breeding_plugevent, name="breeding-plugevents-new"),
    url(r'^(?P<slug>[\w-]+)/?$', views.PlugEventsListStrain.as_view(), name="plugevents-list-strain"),
]
