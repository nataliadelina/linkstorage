from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
# from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm


def register(response):
    if response.method == 'POST':
        # form = UserCreationForm(response.POST)
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    else:
        # form = form = UserCreationForm()
         form = form = RegisterForm()

    return render(response, 'register/register.html', {'form': form})