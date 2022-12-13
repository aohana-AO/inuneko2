from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from logging.config import valid_ident
from re import template
from django.shortcuts import render,redirect
from django.views import View
from allauth.account import views
# Create your views here.
class LoginView(views.LoginView):
    template_name='accounts/login.html'
class LogoutView(views.LogoutView):
    template_name='accounts/logout.html'

    def post(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            self.logout()
        return redirect('/')
class SignupView(views.SignupView):
    template_name='accounts/signup.html'
    #from_class=SignupUserForm
