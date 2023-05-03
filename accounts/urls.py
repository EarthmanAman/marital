# Import django url path
from django.urls import path

# Importing views
from . views import admin_login, user_login, user_sign_up, logout_view, ActivateAccount

# Linking with main url 
app_name = "accounts"

urlpatterns = [
    # Admin login url it calls the admin_login view
    # http://127.0.0.1:8000/accounts/admin
    path('admin', admin_login, name="admin_login"),

    # user login url it calls the user_login view 
    # http://127.0.0.1:8000/accounts/login/
    path('login/', user_login, name="user_login"),

    # user sign up url it calls the user_sign_up view
    # http://127.0.0.1:8000/accounts/user_sign_up
    path('user_sign_up', user_sign_up, name="user_sign_up"),

    # logout url it calls the logout_view view
    # http://127.0.0.1:8000/accounts/logout/
    path('logout/', logout_view, name='logout'),

    path('activate/<uidb64>/<token>/', ActivateAccount.as_view(), name='activate'),
]