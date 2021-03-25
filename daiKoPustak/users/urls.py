from django.urls import path, re_path
from django.contrib.auth import views as auth_views
from . import views
from django.http import HttpResponse
app_name='users'


def login(request):
    return HttpResponse("logged in")


urlpatterns = [
path('',views.HomePage.as_view(),name="home"),
path('login/',auth_views.LoginView.as_view(template_name='users/login.html'),name='login'),
path('signup',views.signUpView,name='signup'),
path('logout/', auth_views.LogoutView.as_view(), name="logout"),
re_path(r'profile/(?P<slug>[-\w]+)/$', views.ProfileView.as_view(), name="userprofile"),
re_path(r'profile/(?P<slug>[-\w]+)/(?P<pk>[-\w]+)/$', views.BookDetailsView.as_view(), name="bookdetail"),
re_path(r'delete_post/(?P<slug>[-\w]+)/(?P<pk>[-\w]+)/$', views.deleteBook, name='deletebook'),
path('all_user/',views.ShowUsersView.as_view(),name="all_user")

]