from django.contrib import admin
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static

from django.contrib.auth import views as auth_views

from accounts.forms import SignInForm, PswdResetForm, SetPswdForm
from accounts import views as accounts_views
from core import views as core_views

urlpatterns = [
    url(r'^$', accounts_views.HomePageView.as_view(), name='home'),
]

urlpatterns = urlpatterns + [
    url(r'^signup$', accounts_views.signup, name='signup'),
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
    url(r'^invest/(?P<plan>\w+)$', core_views.invest, name='invest'),
]

urlpatterns = urlpatterns + [
    url(r'^admin/', admin.site.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)