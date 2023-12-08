from django.urls import path
from . import views

app_name = 'api'

urlpatterns = [
    path('countries', views.countries, name='countries'),
    path('regions', views.regions, name='regions'),
    path('create_user', views.create_user, name='create_user'),
    path('login', views.login, name='login'),
]
