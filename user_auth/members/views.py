from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib.auth import authenticate, login, logout

def home(request):
    return render(request, 'others/home.html', {})

def register(request):
    form = CreateUserForm()
    context = {'form': form}

    if request.method == 'POST':
        form = CreateUserForm(request.POST)  
        if form.is_valid():
            form.save()
            user=form.cleaned_data.get('username')
            messages.success(request,"Account was created for " + user)
            
            return redirect('login')  # ✅ Redirect after successful registration
        else:
            messages.error(request, "There was an error with your registration. Please check the details below.")
    else:
        form = CreateUserForm()
    return render(request, 'user/register.html', context)  # ✅ Added return statement for GET requests

def login_view(request):  
    if request.method== 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        user = authenticate(request, username= username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
    return render(request, 'user/login.html', {})
