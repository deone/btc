from django import forms
from django.contrib.auth.models import User

from .models import Investment, Plan

class InvestmentForm(forms.ModelForm):
    class Meta:
        model = Investment
        exclude = ['time_created']

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        self.plan = kwargs.pop('plan')
        super(InvestmentForm, self).__init__(*args, **kwargs)

        self.label_suffix = ''

        self.fields['user'].initial = self.user
        self.fields['plan'].initial = self.plan
        self.fields['amount'].initial = self.plan.deposit

        self.fields['user'].widget = forms.HiddenInput()
        self.fields['plan'].widget = forms.HiddenInput()
        self.fields['amount'].widget = forms.TextInput(attrs={'class': 'form-control', 'readonly': True})