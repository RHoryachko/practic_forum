from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import EmailUserCreationForm





def register(request):
    if request.method == 'POST':
        form = EmailUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('create_user_profile')
    else:
        form = EmailUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})