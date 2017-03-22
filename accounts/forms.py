from django import forms
from django.conf import settings
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.forms import AuthenticationForm

from .models import Account

from nocaptcha_recaptcha.fields import NoReCaptchaField

import requests

class SignInForm(AuthenticationForm):
    username = forms.EmailField(label=_('Email'), max_length=254,
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email address'}))
    password = forms.CharField(label=_('Password'),
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
    captcha = NoReCaptchaField()

    def __init__(self, *args, **kwargs):
        super(SignInForm, self).__init__(*args, **kwargs)
        self.label_suffix = ''

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

    def clean_full_name(self):
        cleaned_data = super(CreateAccountForm, self).clean()
        full_name = cleaned_data.get('full_name')

        if len(full_name.split(' ')) == 1:
            raise forms.ValidationError(_('Enter first and last names'), code='incomplete_name')

        return full_name

    """ def clean_captcha(self):
        cleaned_data = super(CreateAccountForm, self).clean()
        captcha = cleaned_data.get('captcha')
        print captcha

        response = requests.post(settings.NORECAPTCHA_VERIFY_URL, data={
            'secret': settings.NORECAPTCHA_SECRET_KEY,
            'response': captcha
        })

        print response.status_code, response.json()
        # 200 {u'hostname': u'btc-deone.c9users.io', u'challenge_ts': u'2017-03-20T17:06:10Z', u'success': False}

        return captcha """

    def clean_wallet_address(self):
        cleaned_data = super(CreateAccountForm, self).clean()
        wallet_address = cleaned_data.get('wallet_address')
        address_length = len(wallet_address)

        if address_length < 26 or address_length > 35 or wallet_address[0] not in ['1', '3']:
            raise forms.ValidationError(_('Invalid wallet address'), code='invalid_address')

        return wallet_address

    def clean(self):
        cleaned_data = super(CreateAccountForm, self).clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password and confirm_password:
            if password != confirm_password:
                raise forms.ValidationError(_('Passwords do not match'), code='password_mismatch')

    def save(self):
        first_name, last_name = self.cleaned_data['full_name'].split(' ')
        email = self.cleaned_data['email']
        password = self.cleaned_data['password']

        user = User.objects.create_user(email, email, password)
        user.first_name = first_name
        user.last_name = last_name
        user.save()

        account = Account.objects.create(user=user, wallet_address=self.cleaned_data['wallet_address'])

        return user