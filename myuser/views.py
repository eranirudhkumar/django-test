from django.shortcuts import render, redirect

from .forms import UserRegistrationform
from django.contrib.auth import authenticate,login


# Create your views here.

def login1(request):
    if request.method == 'POST':
        username = request.POST['username']
        psw = request.POST['psw']
        # print(f"Email:{email}")
        # print(f"Password:{psw}")

        user=authenticate(username=username,password=psw)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            pass
    return render(request, 'myuser/login.html')


def register(request):
    if request.method == 'POST':
        # form=UserCreationForm(request.POST)
        form = UserRegistrationform(request.POST)
        print("Hello world")
        if form.is_valid():
            form.save()
            # username=form.cleaned_data.get('username')
            # print("User name:",username)
            return redirect('user-login')
        return redirect('user-register')
    # form=UserCreationForm()
    form = UserRegistrationform()
    context = {
        'form': form
    }
    return render(request,
                  'myuser/register.html',
                  context)
