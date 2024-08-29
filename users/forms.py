from django import forms
from django.contrib.auth.forms import UserCreationForm
from phonenumber_field.formfields import PhoneNumberField

from helpers.storage import upload_user_image


class LoginForm(forms.Form):
    username = forms.CharField(label="Login", max_length=25)
    password = forms.CharField(label="Password", max_length=25, widget=forms.PasswordInput)


class RegisterForm(UserCreationForm):

    phone_number = PhoneNumberField()
    image = forms.ImageField(required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["email"].required = True

    class Meta(UserCreationForm.Meta):
        fields = ("username", "email", "phone_number",
                  "password1", "password2", "image")
