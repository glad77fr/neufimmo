from django import forms
from .models import Subject, Post, Reservation, Profile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


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
           "programme", "user", "topic", "title", "content", "post_image")

        widgets = {'programme': forms.HiddenInput(),
                "user": forms.HiddenInput(),
                "topic": forms.HiddenInput(),
                "title" : forms.TextInput(attrs={'class':'form-control','placeholder' : 'Titre du sujet'})}

class PostModelForm(forms.ModelForm) :
    class Meta:
        model = Post
        fields = ("user", "subject", "content")
        widgets = {"subject" : forms.HiddenInput(),
            "user": forms.HiddenInput(),
            "content": forms.Textarea(attrs={'class':'form-control', 'placeholder': 'Tapez ici votre message'})}
        labels = { "content" : "Message"}

class ReservationModelForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ("user", "programme", "app_ref")
        widgets = {"user" : forms.HiddenInput(),
                   "programme" : forms.HiddenInput(),
                    "app_ref" : forms.TextInput(attrs={'class':'form-control w-25', 'placeholder': "Numéro de l'appartement"})}

        labels = {"user": "utilisateur", "programme" : "programme",
               "app_ref" : "lot appartement"}

    def clean_app_ref(self):
        app_ref = self.cleaned_data["app_ref"]
        if Reservation.objects.filter(app_ref__iexact=app_ref).exists():
            raise ValidationError("Ce lot existe déjà")
        return app_ref