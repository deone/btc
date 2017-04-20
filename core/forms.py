from django import forms

from .models import Investment

class InvestmentForm(forms.ModelForm):
    class Meta:
        model = Investment
        fields = ['amount']

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        self.plan = kwargs.pop('plan')
        super(InvestmentForm, self).__init__(*args, **kwargs)
        self.fields['amount'].initial = self.plan.deposit