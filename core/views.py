from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import FormView

from .models import Investment, Plan
from .forms import InvestmentForm

class PlanListView(ListView):
    model = Plan
    context_object_name = 'plans'

class InvestView(FormView):
    model = Investment
    form_class = InvestmentForm
    template_name = 'core/invest.html'