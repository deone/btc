from django.conf.urls import url
from django.contrib.auth import views as auth_views

from .forms import SignInForm
from . import views

urlpatterns = [
    url(r'^signup$', views.signup, name='signup'),
    url(r'^signin$', auth_views.login, {'template_name': 'accounts/signin.html', 'authentication_form': SignInForm}, name='signin'),
    url(r'^signout$', auth_views.logout, {'next_page': '/'}, name='signout'),
]