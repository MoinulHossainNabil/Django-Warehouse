from django.shortcuts import render, redirect, HttpResponseRedirect
from django.views.generic import View
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import SignupForm
from .decorators import is_user_authenticated


class LoginView(View):
    @method_decorator(is_user_authenticated)
    def get(self, *args, **kwargs):
        return render(self.request, 'login.html', {})

    def post(self, *args, **kwargs):
        username = self.request.POST['username']
        password = self.request.POST['password']
        user = authenticate(self.request, username=username, password=password)
        if user is not None:
            login(self.request, user)
            return redirect('home')
        else:
            messages.info(self.request, "Unauthorized Credentials")
            return redirect('authentication_app:login')


class SignupView(View):
    @method_decorator(is_user_authenticated)
    def get(self, *args, **kwargs):
        form = SignupForm()
        return render(self.request, 'signup.html', {"form": form})

    def post(self, *args, **kwargs):
        form = SignupForm(self.request.POST)
        if form.is_valid():
            form.save()
            messages.success(self.request, "Registration Successful")
            return redirect('authentication_app:login')
        return render(self.request, 'signup.html', {"form": form})


class LogoutView(View):
    def get(self, *args, **kwargs):
        logout(self.request)
        return redirect('authentication_app:login')


class Home(View):
    def get(self, *args, **kwargs):
        return render(self.request, 'home.html', {})