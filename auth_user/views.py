from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
def register(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # username check
        if User.objects.filter(username=username).exists():
            return render(request, 'register.html', {
                'error': 'Username already exists'
            })

        # email check (optional but recommended)
        if User.objects.filter(email=email).exists():
            return render(request, 'register.html', {
                'error': 'Email already registered'
            })

        # create user
        User.objects.create_user(
            username=username,
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name
        )

        return redirect('login_')

    return render(request, 'register.html')



def login_(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {
                'error': 'Invalid username or password'
            })

    return render(request, 'login.html')

@login_required(login_url='login_')
def logout_(request):
    logout(request)
    return redirect('login_')

@login_required(login_url='login_')
def profile(request):
    return render(request,'profile.html')

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

@login_required
def reset_password(request):
    user = request.user  # Get the logged-in user
    context = {}

    if request.method == 'POST':
        # Stage 1: Verify old password
        if 'oldpasw' in request.POST:
            old_password = request.POST['oldpasw']
            # Authenticate user with old password
            u = authenticate(username=user.username, password=old_password)
            if u:
                # Old password is correct, show new password input
                context['new_pass'] = True
            else:
                # Old password is wrong
                context['wrong'] = True
        
        # Stage 2: Set new password
        elif 'newpasw' in request.POST:
            new_password = request.POST['newpasw']
            if new_password:
                user.set_password(new_password)
                user.save()
                # Re-login user after password change
                login(request, user)
                return redirect('profile')  # Redirect to any page you want
            else:
                context['new_pass'] = True  # Stay on new password form if empty

    return render(request, 'reset.html', context)
