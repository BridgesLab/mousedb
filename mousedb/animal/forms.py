"""Forms for use in manipulating objects in the animal app."""

from django.forms import ModelForm
from django import forms

from ajax_select.fields import AutoCompleteSelectField, AutoCompleteSelectMultipleField

from mousedb.animal.models import Animal, Breeding
	
class AnimalForm(ModelForm):
    """This modelform provides fields for modifying animal data.
	
    """
    Father = AutoCompleteSelectField('animals', required=False)	
    Mother = AutoCompleteSelectField('animals', required=False)

    class Meta:
        model = Animal
        fields = "__all__"
		
class MultipleAnimalForm(ModelForm):
	"""This modelform provides fields for entering multiple identical copies of a set of mice.
	
	This form only includes the required fields Background and Strain."""
	count = forms.IntegerField(required=True, help_text="Enter the number of mice to be added")
	class Meta:
		model = Animal
		fields = ['Background', 'Strain', 'Breeding', 'Cage','Rack','Rack_Position','Strain', 'Background', 'Genotype', 'Gender', 'Born', 'Weaned', 'Backcross','Generation', 'Breeding', 'Father', 'Mother', 'Markings', 'Notes']

class MultipleBreedingAnimalForm(ModelForm):
	"""This modelform provides fields for entering multiple pups within a breeding set.
	
	The only fields presented are Born, Weaned, Gender and Count.  Several other fields will be automatically entered based on the Breeding Set entries."""
	count = forms.IntegerField(required=True, help_text="Enter the number of mice to be added")
	class Meta:
		model = Animal
		fields = ['Born', 'Weaned', 'Gender']
	
class BreedingForm(ModelForm):
    """This form provides most fields for creating and entring breeding cage data.
	
    This form is used from the url /mousedb/breeding/new and is a generic create view.  This view includes a datepicker widget for Stat and End dates and autocomplete fields for the Females and Male fields
    """
    Females = AutoCompleteSelectMultipleField('animals-alive')
    Male = AutoCompleteSelectMultipleField('animals-alive')
    class Meta:   
        model = Breeding
        fields = "__all__"
