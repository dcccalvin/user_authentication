from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def login_user(request):
    if request.method == "POST":
        username = request.POST.get("username", "").strip()
        password = request.POST.get("password", "").strip()

        # Prevent login with empty username or password
        if not username or not password:
            messages.error(request, "Username and password are required.")
            return render(request, 'authenticate/login.html', {})  # Stay on the same page

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Invalid username or password.")
            return render(request, 'authenticate/login.html', {})  # Stay on the same page

    return render(request, 'authenticate/login.html', {})

def home(request):
    return render(request, 'authenticate/home.html', {})