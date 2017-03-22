from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from django.contrib.auth import authenticate, login

from .forms import CreateAccountForm

class HomePageView(TemplateView):

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return render(request, 'accounts/index.html')

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