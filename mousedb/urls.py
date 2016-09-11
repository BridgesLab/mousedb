"""Generic base url directives.

These directives will redirect requests to app specific pages, and provide redundancy in possible names."""

from django.conf.urls import url, include
from django.contrib import admin, auth

from tastypie.api import Api
from mousedb.data.api import MeasurementResource, AssayResource, ExperimentResource, StudyResource, TreatmentResource
from mousedb.animal.api import AnimalResource, StrainResource

from ajax_select import urls as ajax_select_urls

from mousedb.views import APIKeyView, logout_view, home

from mousedb.animal.urls import mouse, strain, todo, date, cage, breeding
from mousedb.data.urls import experiment, study, treatment, parameter, cohort
from mousedb.timed_mating import urls as timed_mating_urls

from mousedb import animal, data, timed_mating, veterinary

v1_api = Api(api_name='v1')
v1_api.register(AnimalResource())

v1_api.register(MeasurementResource())
v1_api.register(AssayResource())
v1_api.register(ExperimentResource())
v1_api.register(StudyResource())
v1_api.register(TreatmentResource())


admin.autodiscover()

urlpatterns = (
	#(r'^', 'django.views.generic.simple.direct_to_template', {'template': 'maintenance.html'}),
	url(r'^admin/', include(admin.site.urls)),
    url(r'^api/',include(v1_api.urls)),
    url(r'^api_key/', APIKeyView.as_view(), name="api-keys"),	
	url(r'^accounts/login/?$', auth.views.login, name="login"),
	url(r'^accounts/logout/?$', logout_view, name="logout"),

	url(r'^mouse/', include(mouse)),
	url(r'^mice/', include(mouse)),
	url(r'^animals?/', include(mouse)),
	url(r'^strains?/', include(strain)),
	url(r'^dates?/', include(date)),
	url(r'^breedings?/', include(breeding)),
	url(r'^breeding_cages?/', include(breeding)),
	url(r'^todo/', include(todo)),
	url(r'^cages?/', include(cage)),
	
	url(r'^experiments?/', include(experiment)),
	url(r'^study/', include(study)),
	url(r'^studies/', include(study)),
	url(r'^treatments?/', include(treatment)),
	url(r'^parameters?/', include(parameter)),
    url(r'^cohorts?/', include(cohort)),

	url(r'^plugs?/', include(timed_mating_urls)),
	url(r'^plugevents?/', include(timed_mating_urls)),
	url(r'^plug_events?/', include(timed_mating_urls)),
	url(r'^timedmatings?/', include(timed_mating_urls)),
	url(r'^timed_matings?/', include(timed_mating_urls)),
	
	url(r'^veterinary/', include('mousedb.veterinary.urls')),

    url(r'^ajax_select/', include(ajax_select_urls)),	
	url(r'^index/$', home, name="home"),
	url(r'^$', home)
)

