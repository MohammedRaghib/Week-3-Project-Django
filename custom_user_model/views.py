from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy

def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            error_message = "Invalid credentials"
    else:
        error_message = None
    return render(request, 'login.html', {'error_message': error_message})

def logout_view(request):
    logout(request)
    return redirect("login")

User = get_user_model()

def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        first_name = request.POST.get('first-name')
        last_name = request.POST.get('last-name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        if not all([username, first_name, last_name, email, password, password2]):
            messages.error(request, 'All fields are required.')
            return redirect('register')

        if password != password2:
            messages.error(request, 'Passwords do not match.')
            return redirect('register')

        try:
            User.objects.get(email=email)
            messages.error(request, 'Email is already taken.')
            return redirect('register')
        except User.DoesNotExist:
            pass

        try:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            messages.success(request, 'Registration successful. You can now log in.')
            return redirect('login')
        except ValidationError as e:
            messages.error(request, f'Error: {", ".join(e.messages)}')
            return redirect('register')

    return render(request, 'register.html')

def error_404(request, exception):
    return render(request, '404.html')