from django.forms import ModelForm
from .models import Programme

def ProgrammeForm(ModelForm):
    class Meta:
        model = Programme
        fields = ['nom', 'promoteur', 'description', 'date_livraison_ini', 'date_livraison_act']

