from django.shortcuts import render
from django.views.generic.base import TemplateView

from .forms import CreateAccountForm

class HomePageView(TemplateView):

    template_name = 'accounts/index.html'

def create(request):
    if request.method == 'POST':
        form = CreateAccountForm(request.POST, label_suffix='')
        if form.is_valid():
            form.save()
            # send mail
            # log user in
            # redirect
    else:
        form = CreateAccountForm(label_suffix='')

    return render(request, 'accounts/signup.html', {'form': form})