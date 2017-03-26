from django.conf.urls import url
from django.contrib.auth import views as auth_views

from .forms import SignInForm, PswdResetForm
from . import views

urlpatterns = [
    url(r'^signup$', views.signup, name='signup'),
    url(r'^signin$', auth_views.login, {'template_name': 'accounts/signin.html', 'authentication_form': SignInForm}, name='signin'),
    url(r'^signout$', auth_views.logout, {'next_page': '/'}, name='signout'),
    url(r'^accounts/password_reset$', auth_views.password_reset,
      {'template_name': 'accounts/password_reset_form.html', 'password_reset_form': PswdResetForm},
      name='password_reset'),
]