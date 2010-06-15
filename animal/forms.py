"""Forms for use in manipulating objects in the animal app."""

from django.forms import ModelForm
from django import forms

from ajax_select.fields import AutoCompleteSelectMultipleField, AutoCompleteSelectField

from mousedb.animal.models import Animal, Breeding
	
class AnimalForm(ModelForm):
	"""This modelform provides fields for modifying animal data.
	
	It includes all fields except CageID (will be deprecated) and Alive (which is automattically set upon saving the animal).
	This form also automatically loads javascript and css for the datepicker jquery-ui widget.  It also includes auto"""
	Father = AutoCompleteSelectField('animal', required=False)
	Mother = AutoCompleteSelectField('animal', required=False)
	class Meta:
		model = Animal
		exclude = ['CageID', 'Alive']
	class Media:
		css = {
			'all': ('javascript/jquery-ui/css/custom-theme/jquery-ui-1.7.2.custom.css','javascript/jquery-autocomplete/jquery.autocomplete.css', 'css/iconic.css')
				}
		js = ('javascript/jquery-1.3.2.js','javascript/jquery-ui/js/jquery-ui-1.7.2.custom.min.js', 'javascript/jquery-autocomplete/jquery.autocomplete.js')


class BreedingForm(ModelForm):
    """This form provides most fields for creating and entring breeding cage data.
	
    This form is used from the url /mousedb/breeding/new and is a generic create view.  The only excluded field is CageID, as this feature will be deprecated.  This view includes a datepicker widget for Stat and End dates and autocomplete fields for the Females and Male fields
    """
    Male = AutoCompleteSelectMultipleField('animal', required=False)
    Females = AutoCompleteSelectMultipleField('animal', required=False)
    class Meta:
        model = Breeding
        exclude = ['CageID', 'Active']
    class Media:
		css = {
			'all': ('javascript/jquery-ui/css/custom-theme/jquery-ui-1.7.2.custom.css','javascript/jquery-autocomplete/jquery.autocomplete.css', 'css/iconic.css')
				}
		js = ('javascript/jquery-1.3.2.js','javascript/jquery-ui/js/jquery-ui-1.7.2.custom.min.js', 'javascript/jquery-autocomplete/jquery.autocomplete.js')




