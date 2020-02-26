from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .forms import UserRegisterForm

# loads register page and redirects to index once user has registers
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

# loads index page when user is logged in, otherwise loads login page
def index(request):
    if (request.user.is_authenticated):
        return render(request, 'bookdata/index.html')
    else:
        return redirect('login')
