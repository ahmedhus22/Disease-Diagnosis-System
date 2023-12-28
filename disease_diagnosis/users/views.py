from django.shortcuts import render
from django.shortcuts import redirect
from .forms import UserRegisterForm
from django.contrib import messages
from django.conf import settings

User = settings.AUTH_USER_MODEL

def register(request):
    if request.method =='POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('diagnosis_system-home')
        
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})
