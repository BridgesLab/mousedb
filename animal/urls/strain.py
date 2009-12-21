from django.conf.urls.defaults import *

from mousedb.animal.models import Strain

urlpatterns = patterns('',
        (r'^$', 'mousedb.animal.views.strain_list'),
		(r'^new/$', 'django.views.generic.create_update.create_object', {
		'model': Strain, 
		'template_name': 'strain_form.html', 
		'login_required':True,
		'post_save_redirect':'/mousedb/strain/'
		}),
	(r'^(?P<object_id>\d*)/update/$', 'django.views.generic.create_update.update_object', {
		'model': Strain, 
		'template_name': 'strain_form.html', 
		'login_required':True,
		'post_save_redirect':'/mousedb/strain/',
		}),
	(r'^(?P<object_id>\d*)/delete/$', 'django.views.generic.create_update.delete_object', {
		'model': Strain, 
		'login_required':True,
		'post_delete_redirect':'/mousedb/strain/',
		}),
        (r'^(?P<strain>.*)/$', 'mousedb.animal.views.strain_detail'),
        (r'^(?P<strain>.*)/all$', 'mousedb.animal.views.strain_detail_all'),
)
