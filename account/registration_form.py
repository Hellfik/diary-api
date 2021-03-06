from django import forms
from django.contrib.auth.forms import UserCreationForm


from account.models import Account

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=60, help_text="Required. Add a valid address")


    class Model:
        model = Account
        fields = ("email", "username", "password1", "password2")