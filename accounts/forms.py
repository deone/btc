from django import forms
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from nocaptcha_recaptcha.fields import NoReCaptchaField

class CreateAccountForm(forms.Form):
    full_name = forms.CharField(label=_('Full Name'), widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'First Name Last Name'
    }))
    email = forms.EmailField(label=_('Email'), widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'Email address'
    }))
    password = forms.CharField(label=_('Password'), widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Password'
    }))
    confirm_password = forms.CharField(label=_('Confirm Password'), widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Type password again'
    }))
    wallet_address = forms.CharField(label=_('Wallet Address'), widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Wallet Address'
    }), help_text="Ensure this is correct. We won't be responsible for errors caused by an incorrect address.")
    captcha = NoReCaptchaField()
    agree_to_terms = forms.BooleanField()

    """ def clean_name(self):
        cleaned_data = super(CreateAccountForm, self).clean()
        name = cleaned_data.get('name')

        if len(name.split(' ')) == 1:
            raise forms.ValidationError(_('Enter first and last names'), code='incomplete_name')

        return name

    def clean(self):
        cleaned_data = super(CreateAccountForm, self).clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password and confirm_password:
            if password != confirm_password:
                raise forms.ValidationError(_('Passwords do not match'), code='password_mismatch') """

    def save(self):
        print self.cleaned_data