from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from django.contrib.auth import authenticate, login

from .forms import CreateAccountForm
from core.models import Investment

class HomePageView(TemplateView):

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['investments'] = Investment.objects.filter(user=self.request.user)
        return context

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            context = self.get_context_data(**kwargs)
            if not context['investments']:
                return redirect('plans')
            return render(request, 'core/investment_list.html', context)

        return render(request, 'index.html')

def signup(request):
    if request.method == 'POST':
        form = CreateAccountForm(request.POST, label_suffix='')
        if form.is_valid():
            form.save()

            username = form.cleaned_data['email']
            password = form.cleaned_data['password']

            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = CreateAccountForm(label_suffix='')

    return render(request, 'accounts/signup.html', {'form': form})