from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def login_user(request):
    if request.method == "POST":
        username = request.POST.get("username", "").strip()
        password = request.POST.get("password", "").strip()
        print(f"Submitted Username: {username}, Password: {password}")  # Debug

        if not username or not password:
            print("Empty fields detected")  # Debug
            messages.error(request, "Username and password are required.")
            return render(request, 'authenticate/login.html')

        user = authenticate(request, username=username, password=password)
        print(f"Authenticated User: {user}")  # Debug

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Invalid username or password.")
            return render(request, 'authenticate/login.html')
    else:
        messages.info(request, "Test: Messages are working!")  # Debug
        return render(request, 'authenticate/login.html')
    # else:
    #     messages.info(request, "Test message on GET request.")
    #     return render(request, 'authenticate/login.html', {})
    
    return render(request, 'authenticate/login.html', {})  # Show login page if GET request

def home(request):
    return render(request, 'authenticate/home.html', {})