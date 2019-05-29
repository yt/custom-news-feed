from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import RegisterForm

def user_register(request):

    template = 'users/register.html'
    
    if request.method != 'POST':
        form = RegisterForm()
        return render(request, template, { 'form': form })


    form = RegisterForm(request.POST)
    
    if not form.is_valid():
        return render(request, template, { 'form': form })


    if User.objects.filter(username=form.cleaned_data['username']).exists():
        return render(request, template, {
            'form': form, 
            'error_message': 'Username already exists.'
        })
    elif User.objects.filter(email=form.cleaned_data['email']).exists():
        return render(request, template, {
            'form': form, 
            'error_message': 'Email already exists.'
        })
    elif form.cleaned_data['password'] != form.cleaned_data['password_repeat']:
        return render(request, template, {
            'form': form, 
            'error_message': 'Passwords do not match.'
        })


    user = User.objects.create_user(
        form.cleaned_data['username'], 
        form.cleaned_data['email'], 
        form.cleaned_data['password']
    )

    user.first_name = form.cleaned_data['first_name']
    user.last_name = form.cleaned_data['last_name']
    user.phone_number = form.cleaned_data['phone_number']
    user.save()
    
    # TODO Login the user here
    # TODO redirect to accounts page HttpResponseRedirect()

    return render(request, template, {'form': form})
