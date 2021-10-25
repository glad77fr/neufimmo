from django import forms
from .models import Subject
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _


class SubjectModelForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = (
           "programme", "topic", "title", "content")

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'Titre du sujet', 'width':'30px'}),
            "programme": forms.Select(attrs={'class': 'form-control'}),
            'topic': forms.Select(attrs={'class': 'form-control'}),
            "content": forms.Textarea(attrs={'class': 'form-control', 'placeholder' : 'Contenu du sujet'}),
        }

        labels = {'title' : 'Titre', 'content' : 'Message', 'topic':'Thème','class': 'form-text'}