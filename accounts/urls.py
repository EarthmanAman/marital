from django.urls import path

from . views import admin_login, user_login, user_sign_up

app_name = "accounts"

urlpatterns = [
    path('admin', admin_login, name="admin_login"),
    path('login/', user_login, name="user_login"),
    path('user_sign_up', user_sign_up, name="user_sign_up")
]