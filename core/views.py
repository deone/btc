from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.base import TemplateView

from .models import Investment, Plan

class PlanListView(ListView):
    model = Plan
    context_object_name = 'plans'

class InvestView(TemplateView):
    template_name = 'core/invest_success.html'

    def dispatch(self, request, *args, **kwargs):
        plan = Plan.objects.get(name=kwargs['plan'])
        investment = Investment.objects.create(user=request.user, plan=plan, amount=plan.deposit)
        return render(request, self.template_name, {'investment': investment})