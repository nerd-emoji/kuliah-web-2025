from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login 
from django.contrib.auth.decorators import login_required  

@login_required(login_url='/dashboard/signin/')
def index(request):
    return render(request, 'dashboard.html')

home = index

def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/dashboard/') 
        else:
            messages.error(request, 'Invalid username or password.')
            return render(request, 'signin.html', {'username': username})
    return render(request, 'signin.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        p1 = request.POST.get('password1', '')
        p2 = request.POST.get('password2', '')

        errors = []
        if not username:
            errors.append('Username is required.')
        if not p1:
            errors.append('Password is required.')
        if p1 != p2:
            errors.append('Passwords do not match.')
        if User.objects.filter(username=username).exists():
            errors.append('Username already taken.')

        if errors:
            return render(request, 'signup.html', {'errors': errors, 'username': username})

        user = User.objects.create_user(username=username, password=p1)
        user.save()
        messages.success(request, 'Account created. Please sign in.')
        return redirect('/dashboard/signin/')

    return render(request, 'signup.html')

def forgot_password(request):
    if request.method == 'POST':
        email = request.POST.get('email', '').strip()

        messages.info(request, 'If an account with that email exists, a password reset link has been sent.')
        return redirect('dashboard:forgot-password')

    return render(request, 'forgot-password.html')