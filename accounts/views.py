from django.shortcuts import redirect, render
from .forms import UserRegistrationForm
from django.contrib.auth.forms import AuthenticationForm

from django.contrib.auth import authenticate, login,logout
from django.contrib import messages


def home(request):
    return render(request, 'accounts/home.html')

""" A basic register view that on get displays a blank form,
    on post processes the form data and displays a 
    success message """
def user_register(request):
    form = UserRegistrationForm()
    context = {'form': form}
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.add_message(request, messages.SUCCESS, 'User created successfully')
            return redirect('accounts:home')
            
    return render(request, 'accounts/register.html',context)


""" A basic login form that on get return blank login form 
    and on post authenthicates the user and displays message
"""
def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"{username} logged in successfully.")
                return redirect('accounts:home')
            else:
                messages.error(request, "Wrong credentials , please try again")
    else:
        form = AuthenticationForm()
    context = {'form': form}
    return render(request, 'accounts/login.html', context)


def user_logout(request):
    logout(request)
    return redirect('accounts:home')