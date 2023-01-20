from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout

def admin_login(request):
    template_name = "./admin_login.html"
    return render(request, template_name)

def user_login(request):
    template_name = "./user_login.html"
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('portal:dashboard')
        else:
            return render(request, template_name, {'error': 'Invalid login credentials'})
    else:
        return render(request, template_name)

def user_sign_up(request):
    template_name = "./user_sign_up.html"
    return render(request, template_name)


def logout_view(request):
    logout(request)
    return redirect('main:index')