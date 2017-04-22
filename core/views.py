from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import FormView

from .models import Investment, Plan
from .forms import InvestmentForm

class PlanListView(ListView):
    model = Plan
    context_object_name = 'plans'

class InvestView(FormView):
    form_class = InvestmentForm
    template_name = 'core/invest.html'

    def plan(self):
        return self.plan

    def get_form_kwargs(self):
        plan_name = self.kwargs['plan_name']
        self.plan = Plan.objects.get(name=plan_name)

        kwargs = super(InvestView, self).get_form_kwargs()
        kwargs['plan'] = self.plan
        kwargs['user'] = self.request.user
        return kwargs