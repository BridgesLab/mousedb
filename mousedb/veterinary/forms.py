
from django.forms import ModelForm

from ajax_select.fields import AutoCompleteSelectField, AutoCompleteSelectMultipleField

from mousedb.veterinary.models import MedicalIssue

class MedicalIssueForm(ModelForm):
    animal = AutoCompleteSelectField('animals')

    class Meta:
        model = MedicalIssue
        fields = '__all__'
