from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def home(request):
    
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            message.success(request, "You have been logged in")
            return redirect('home')

    return render(request, 'home.html', {})

def login_user(request):
    pass

def logout_user(request):
    pass