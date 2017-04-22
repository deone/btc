from django.urls import reverse
from django.shortcuts import render, redirect
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
        self.plan_name = self.kwargs['plan_name']
        self.plan = Plan.objects.get(name=self.plan_name)

        kwargs = super(InvestView, self).get_form_kwargs()
        kwargs['plan'] = self.plan
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.save()
        return redirect(reverse('invest', kwargs={'plan_name': self.plan_name}))