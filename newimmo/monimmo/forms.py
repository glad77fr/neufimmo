from django import forms
from .models import Subject, Post
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):

    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'placeholder': 'Saisir votre identifiant',
                                                             'class': 'form-control',
                                                             }))
    password1 = forms.CharField(max_length=50,
                               required=True,
                               widget=forms.PasswordInput(attrs={'placeholder': 'Saisir votre mot de passe',
                                                                 'class': 'form-control',
                                                                 'data-toggle': 'password',
                                                                 'id': 'password',
                                                                 }))
    password2 = forms.CharField(max_length=50,
                                required=True,
                                widget=forms.PasswordInput(attrs={'placeholder': 'Ressaisir votre mot de passe',
                                                                  'class': 'form-control',
                                                                  'data-toggle': 'password',
                                                                  'id': 'password',
                                                                  }))

    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.',
                                 widget=forms.TextInput(attrs={'placeholder': 'Saisir votre prénom',
                                                               'class': 'form-control',
                                                               }))

    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.',
                                widget=forms.TextInput(attrs={'placeholder': 'Saisir votre nom',
                                                               'class': 'form-control',
                                                               }))

    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.',required=False,
                             widget=forms.TextInput(attrs={'placeholder': 'Saisir votre adresse email',
                                                               'class': 'form-control',
                                                               }))
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )

class SubjectModelForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = (
           "programme", "topic", "title", "content")

        widgets = {'programme': forms.HiddenInput(),
                  "topic": forms.HiddenInput(),
                  "title" : forms.TextInput(attrs={'class':'form-control','placeholder' : 'Titre du sujet'}),
                  "content": forms.Textarea(attrs={'class': 'form-control', 'placeholder' : 'Contenu du sujet'})}

class PostModelForm(forms.ModelForm) :
    class Meta:
        model = Post
        fields = ("subject", "content")
        widgets = {"subject" : forms.HiddenInput(),
            "content": forms.Textarea(attrs={'class':'form-control', 'placeholder': 'Tapez ici votre message'})}
        labels = { "content" : "Message"}