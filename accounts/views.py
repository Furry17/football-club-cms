from django.contrib.auth import login
from django.shortcuts import redirect, render

from . import forms


def login_view(request):
    if request.method == "POST":
        form = forms.LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("home")
    else:
        form = forms.LoginForm()
    return render(request, "accounts/login.html", {"form": form})

def logout_view(request):
    from django.contrib.auth import logout
    logout(request)
    return redirect("home")


def register_view(request):
    if request.method == "POST":
        form = forms.RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("register_success")
    else:
        form = forms.RegisterForm()
    return render(request, "accounts/register.html", {"form": form}) 

def register_success_view(request):
    return render(request, "accounts/register_success.html") 