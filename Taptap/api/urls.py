from django.urls import path
from . import views

app_name = 'api'

urlpatterns = [
    path('countries', views.countries, name='countries'),
    path('regions', views.regions, name='regions'),
    path('create_user', views.create_user, name='create_user'),
    path('login', views.login, name='login'),
    path('posts', views.posts, name='posts'),  # if type = 0 show all posts
    path('user_posts', views.user_posts, name='user_posts'),
    path('post_hitcount', views.post_hitcount, name='post_hitcount'),
    path('search_post', views.search_post, name='search_post'),  # if type = 0 search in all posts
    path('create_post', views.create_post, name='create_post'),
    path('post_detail', views.post_detail, name='post_detail'),
]
