from django.conf.urls import url
from django.contrib.auth import views as auth_views

from .forms import SignInForm, PswdResetForm, SetPswdForm
from . import views

urlpatterns = [
    url(r'^signup$', views.signup, name='signup'),
    url(r'^signin$', auth_views.login,
      {
        'template_name': 'accounts/signin.html',
        'authentication_form': SignInForm
      }, name='signin'),
    url(r'^signout$', auth_views.logout, {'next_page': '/'}, name='signout'),
    url(r'^password_reset$', auth_views.password_reset,
      {
        'template_name': 'accounts/password_reset_form.html',
        'password_reset_form': PswdResetForm,
        'email_template_name': 'accounts/password_reset_email.html'
      }, name='password_reset'),
    url(r'^password_reset/done$', auth_views.password_reset_done,
      {
        'template_name': 'accounts/password_reset_done.html'
      }, name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})$', auth_views.password_reset_confirm,
      {
        'template_name': 'accounts/password_reset_confirm.html',
        'set_password_form': SetPswdForm
      }, name='password_reset_confirm'),
    url(r'^reset/done$', auth_views.password_reset_complete,
      {
        'template_name': 'accounts/password_reset_complete.html'
      }, name='password_reset_complete'),
]