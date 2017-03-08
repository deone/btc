from django import forms
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

class CreateAccountForm(forms.Form):
    full_name = forms.CharField(label=_('Full Name'), widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'First name and last name'
    }))
    email = forms.EmailField(label=_('Email'), widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'email address'
    }))
    password = forms.CharField(label=_('Password'), widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Password'
    }))
    confirm_password = forms.CharField(label=_('Confirm Password'), widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Type password again'
    }))

    def clean_name(self):
        cleaned_data = super(CreateAccountForm, self).clean()
        name = cleaned_data.get('name')

        if len(name.split(' ')) == 1:
            raise forms.ValidationError(_('Enter first and last names'), code='incomplete_name')

        return name

    def clean_email(self):
        cleaned_data = super(CreateAccountForm, self).clean()
        email = cleaned_data.get('email')

        # Make an API call here
        response = requests.get(settings.ACCOUNT_GET_URL, params={'email': email})

        if response.status_code == 200:
            raise forms.ValidationError(_('User already exists'), code='user_exists')

        return email

    def clean(self):
        cleaned_data = super(CreateAccountForm, self).clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password and confirm_password:
            if password != confirm_password:
                raise forms.ValidationError(_('Passwords do not match'), code='password_mismatch')

    def save(self):
        pass