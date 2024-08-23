from django import forms
from apps.accounts.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import RegexValidator

phone_regex = RegexValidator(
    regex=r"^\+998\d{9}$",
    message="Phone number must be entered in the format: '+998XXXXXXXX'. Up to 13 digits allowed.",
)

password_regex = RegexValidator(
    regex=r"^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$",
    message="""
    Parol to'liq emas. Minimum 8 ta belgi, kamida bitta 
    katta kichik harf, bitta katta harf, bitta raqam va 
    bitta simvol bo'lishi kerak.""",
)


class UserForm(forms.ModelForm):
    
    password1 = forms.CharField(
        label=("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        # validators=[password_regex],
    )
    password2 = forms.CharField(
        label=("Password confirmation"),
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        strip=False,
    )

    phone = forms.CharField(validators=[phone_regex], max_length=13)

    def clean(self):
        cleaned_data = super().clean()
        pass1 = cleaned_data.get("password1")
        pass2 = cleaned_data.get("password2")

        if pass1 != pass2:
            raise forms.ValidationError("Parollar bir xil emas")
        return cleaned_data 

    class Meta: 
        model = User
        fields = ['phone',]


