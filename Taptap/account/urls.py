from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('user_login', views.user_login, name='user_login'),
    path('user_logout', views.user_logout, name='user_logout'),
    path('signup', views.signup, name='signup'),
    path('home', views.home, name='home'),
    path('profile', views.profile, name='profile'),
    path('validate_username_ajax', views.validate_username_ajax, name='validate_username_ajax'),
]