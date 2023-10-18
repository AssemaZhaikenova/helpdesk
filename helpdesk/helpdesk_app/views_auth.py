from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect


def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(username=email, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect("/")
        else:
            message = 'Неверный логин или пароль'
            return render(request, 'helpdesk_app/login.html', {'message': message})
    else:
        return render(request, 'helpdesk_app/login.html')


def logout_view(request):
    logout(request)
    return redirect("/")

