from django.shortcuts import render, redirect, render_to_response
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.shortcuts import HttpResponseRedirect
from .forms import CustomUserCreationForm
from django.contrib import messages

# Create your views here.


def signup_view(request):
    if request.method == 'POST':
        f = CustomUserCreationForm(request.POST)
        if f.is_valid():
            f.save()
            return redirect('blog:home')
    else:
        f = CustomUserCreationForm()
    return render(request, 'accounts/signup.html', {'form': f})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            #log in the user
            user = form.get_user()
            login(request,user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('blog:home')
    else:
        form = AuthenticationForm()

    return render(request, 'accounts/login.html',{'form':form })

def logout_view(request):
    logout(request)
    return HttpResponseRedirect("/accounts/login/")
