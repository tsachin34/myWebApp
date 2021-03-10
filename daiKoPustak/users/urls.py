from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.http import HttpResponse
app_name='users'


def login(request):
    return HttpResponse("logged in")


urlpatterns = [
path('login/',auth_views.LoginView.as_view(template_name='users/login.html'),name='login'),
path('signup',views.signUpView,name='signup'),
path('logout/', auth_views.LogoutView.as_view(), name="logout"),
path('logged',login,name='logged')
]