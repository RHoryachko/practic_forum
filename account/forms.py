from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User




class EmailUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'real-input'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'real-input'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'real-input'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'real-input'}))


    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(EmailUserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user