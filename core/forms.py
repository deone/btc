from django import forms
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

from .models import Investment, Plan

class InvestmentForm(forms.ModelForm):
    plan = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'readonly': True}))

    class Meta:
        model = Investment
        exclude = ['plan', 'time_created']

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        self.plan = kwargs.pop('plan')
        super(InvestmentForm, self).__init__(*args, **kwargs)

        self.label_suffix = ''

        self.fields['user'].initial = self.user
        self.fields['plan'].initial = str(self.plan.deposit) + ' BTC'
        self.fields['plan'].label = _('Deposit')

        self.fields['user'].widget = forms.HiddenInput()

    def save(self, commit=True):
        deposit = self.cleaned_data['plan'].split(' ')[0]
        plan = Plan.objects.get(deposit=deposit)
        self.instance.plan = plan

        return super(InvestmentForm, self).save(commit)