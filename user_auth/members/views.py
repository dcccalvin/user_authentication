from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm

def home(request):
    return render(request, 'others/home.html', {})

def register(request):
    form = CreateUserForm()
    context = {'form': form}

    if request.method == 'POST':
        form = CreateUserForm(request.POST)  
        if form.is_valid():
            form.save()
            return redirect('home')  # ✅ Redirect after successful registration

    return render(request, 'user/register.html', context)  # ✅ Added return statement for GET requests

def login_view(request):  # ✅ Renamed function to avoid conflict with `login` import
    return render(request, 'user/login.html', {})
