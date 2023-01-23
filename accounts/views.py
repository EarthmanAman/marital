from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.conf import settings

from . models import CustomUser as User

def admin_login(request):
    template_name = "./admin_login.html"
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
    context = {"first_name":'', "last_name":'', "phone_number":'', "address":'', "error":'', "email":''}
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        phone_number = request.POST.get("phone_number")
        address = request.POST.get("address")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")
        if password != confirm_password:
            context["first_name"] = first_name
            context["last_name"] = last_name
            context["email"] = email
            context["phone_number"] = phone_number
            context["address"] = address

            context["error"] = "Password do not match"
        else:
            user = User(first_name=first_name, last_name=last_name, email=email, username=email, phone_number=phone_number, address=address)
            user.set_password(password)
            user.save()
            return redirect("accounts:user_login")

    return render(request, template_name, context)


def logout_view(request):
    logout(request)
    return redirect('main:index')