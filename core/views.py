from django.shortcuts import render
from django.views.generic.edit import FormView

from .models import Investment
from .forms import InvestmentForm

class InvestView(FormView):
    model = Investment
    form_class = InvestmentForm
    template_name = 'core/invest.html'