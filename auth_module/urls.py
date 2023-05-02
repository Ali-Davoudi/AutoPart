from django.urls import path, include
from auth_module.views import (LoginView, RegisterView, AccountActivationView, LogoutView, ForgetPasswwordView, \
                               ResetPasswordView)

urlpatterns = [
    path('login/', LoginView.as_view(), name='login_page'),
    path('register', RegisterView.as_view(), name='register_page'),
    path('activate-account/<active_code>', AccountActivationView.as_view(), name='account_activation'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('forget-password', ForgetPasswwordView.as_view(), name='forget_password_page'),
    path('reset-password/<active_code>', ResetPasswordView.as_view(), name='reset_password_page'),
    path('', include('social_django.urls', namespace='social'))   # For google authentication
]
