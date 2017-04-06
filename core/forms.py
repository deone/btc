from django import forms

from .models import Investment

class InvestmentForm(forms.ModelForm):
    class Meta:
        model = Investment
        fields = ['amount']

    def __init__(self, *args, **kwargs):
        super(InvestmentForm, self).__init__(*args, **kwargs)
        self.label_suffix = ''
        self.fields['amount'].widget = forms.NumberInput(attrs={'class': 'form-control'})