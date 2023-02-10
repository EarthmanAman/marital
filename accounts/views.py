from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout

# Importing the User Model
from . models import CustomUser as User

def admin_login(request):
    """
    Admin login view.
    It accept an http request as a parameter and renders the ./admin_login.html
    Also accept POST data to login user
    """

    # The login template
    template_name = "./admin_login.html"

    # Check if the user submit credentials to login
    # If he submitted try to login the user in else just render the login page
    if request.method == 'POST':
        email = request.POST['email'] # Get submitted email
        password = request.POST['password'] # Get submitted password

        # Check if the user is in the database and credentials are correct
        user = authenticate(request, username=email, password=password)

        # If the user is present and credentials are correct
        if user is not None:
            # Login the user
            login(request, user)

            # redirect the user to the admin dashboard
            return redirect('portal:dashboard')
        else:
            # Else if not render the login page again and pass an error message
            return render(request, template_name, {'error': 'Invalid login credentials'})
    else:
        # Rendering the login page
        return render(request, template_name)

def user_login(request):

    # The user login template
    template_name = "./user_login.html"

    # Check if the user submit credentials to login
    # If he submitted try to login the user in else just render the user login page
    if request.method == 'POST':
        email = request.POST['email'] # Get submitted email
        password = request.POST['password'] # Get submitted password

        # Check if the user is in the database and credentials are correct
        user = authenticate(request, username=email, password=password)

        # If the user is present and credentials are correct
        if user is not None:
            login(request, user)

             # redirect the user to the user dashboard
            return redirect('portal:dashboard')
        else:
            return render(request, template_name, {'error': 'Invalid login credentials.'})
    else:
        return render(request, template_name)

def user_sign_up(request):

    # The user sign up template
    template_name = "./user_sign_up.html"

    # Information to be passed to the frontend
    context = {"first_name":'', "last_name":'', "phone_number":'', "address":'', "error":'', "email":''}

    # Check if method is POST and try to create the user using the information they provided
    # Else render the signup page
    if request.method == "POST":

        # Getting information from user
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        phone_number = request.POST.get("phone_number")
        address = request.POST.get("address")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        # Check if password match
        # If they don't render the signup page with error
        # Else proceed to register the user
        if password != confirm_password:
            # Updating the information to be passed to template in order to prevent user type everything again
            context["first_name"] = first_name
            context["last_name"] = last_name
            context["email"] = email
            context["phone_number"] = phone_number
            context["address"] = address

            context["error"] = "Password do not match"
        else:
            # Registering user
            user = User(first_name=first_name, last_name=last_name, email=email, username=email, phone_number=phone_number, address=address)

            # Set password
            user.set_password(password)
            user.save()

            # Redirect to login
            return redirect("accounts:user_login")

    return render(request, template_name, context)


def logout_view(request):
    # Calling the django logout method to logout user
    logout(request)

    # Redirect to homepage
    return redirect('main:index')