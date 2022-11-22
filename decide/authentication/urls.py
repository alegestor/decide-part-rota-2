from django.urls import include, path
from rest_framework.authtoken.views import obtain_auth_token

from .views import GetUserView, LogoutView, RegisterView, loginForm, registerForm



urlpatterns = [
    path('', welcome),
    path('login/', login),
    path('register/', register),
    path('logout/', LogoutView.as_view()),
    path('getuser/', GetUserView.as_view()),
    path('register/', RegisterView.as_view()),
    path('loginForm/', loginForm),
    path('registerForm/', registerForm)
]
