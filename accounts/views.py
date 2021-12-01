from django.shortcuts import redirect, render
from .forms import UserRegistrationForm
from django.contrib.auth.forms import AuthenticationForm

from django.contrib.auth import authenticate, login
from django.contrib import messages


def home(request):
    return render(request, 'accounts/home.html')

def user_register(request):
    form = UserRegistrationForm()
    context = {'form': form}
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('accounts:home')
            
    return render(request, 'accounts/register.html',context)


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
                