from django import forms
from .models import Subject

class SubjectModelForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = (
            "title",  "topic", "content")

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control col-md-4', 'placeholder' : 'Titre du sujet', 'wight':"30"}),
            'topic': forms.Select(attrs={'class': 'form-control col-md-4'}),
            "content": forms.Textarea(attrs={'class': 'form-control col-md-10', 'placeholder' : 'Contenu du sujet'}),
        }

        labels = {'title' : 'Titre', 'content' : 'Message', 'topic':'Thème','class': 'form-text'}