from django.shortcuts import render
from .forms import LoginForm, RegisterForm
from django.http import HttpResponseRedirect
from django.urls import reverse


def login(request):
    return render(request, 'authapp/login.html')


def register(request):

    if request.method == 'POST':
        register_form = RegisterForm(data=request.POST)
        if register_form.is_valid():
            register_form.save()
            return HttpResponseRedirect(reverse('authapp:login'))
    else:
        register_form = RegisterForm()
    context = {'register_form': register_form}
    return render(request, 'authapp/register.html', context)