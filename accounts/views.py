from django.shortcuts import render
from django.views.generic.base import TemplateView

from .forms import CreateAccountForm

class HomePageView(TemplateView):

    template_name = 'accounts/index.html'

def create(request):
    """ if request.method == 'POST':
        form = CreateAccountForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = CreateAccountForm() """

    return render(request, 'accounts/signup.html')