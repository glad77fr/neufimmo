from django import forms
from .models import Subject

class SubjectModelForm(forms.ModelForm):
    class Meta:
        model = Subject

        fields = (
            "title", "content")

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'Titre du sujet'}),
            "content": forms.Textarea(attrs={'class': 'form-control', 'placeholder' : 'Contenu du sujet'}),
        }

        labels = {'title' : 'Titre', 'content' : 'Message', 'class': 'form-text'}