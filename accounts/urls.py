from django.conf.urls import url
from . import views
from django.conf.urls import include, url
from django.contrib.auth.forms import (
    AuthenticationForm, PasswordChangeForm, PasswordResetForm, SetPasswordForm,
)




app_name='accounts'

urlpatterns = [
    url(r'^signup/$',views.signup_view, name="signup"),
    url(r'^login/$',views.login_view, name="login"),
    url(r'^logout/$',views.logout_view, name="logout"),
]