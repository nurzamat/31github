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

    # API
    url(r'^api/categories/$', api_views.categories, name='categories'),
    url(r'^api/countries/$', api_views.countries, name='countries'),
    url(r'^api/regions/$', api_views.regions, name='regions'),
    url(r'^api/register/$', api_views.create_user, name='create_user'),
    url(r'^api/login/$', api_views.login, name='login'),
    url(r'^api/category/(?P<post_type>[0-9]+)/posts/$', api_views.posts, name='posts'),  # if type = 0 show all posts
    url(r'^api/user/(?P<user_id>[0-9]+)/posts/$', api_views.user_posts, name='api_user_posts'),
    url(r'^api/post/(?P<post_id>[0-9]+)/hitcount/$', api_views.post_hitcount, name='post_hitcount'),
    url(r'^api/posts/search/$', api_views.search_post, name='search_post'),  # if type = 0 search in all posts
    url(r'^api/posts/create/$', api_views.create_post, name='create_post'),
    url(r'^api/post/(?P<post_id>[0-9]+)/$', api_views.post_detail, name='post_detail'),
    url(r'^api/user/(?P<user_id>[0-9]+)/orders/$', api_views.user_orders, name='api_user_orders'),
    url(r'^api/orders/(?P<order_id>[0-9]+)/items/$', api_views.api_order_items, name='api_order_items'),
    url(r'^api/orders/create/$', api_views.create_order, name='api_create_order'),
    url(r'^api/orders/(?P<order_id>[0-9]+)/status/(?P<status>[0-9]+)$', api_views.update_order,
        name='api_update_order'),
    url(r'^api/order/(?P<order_id>[0-9]+)/item/add/$', api_views.add_item, name='api_add_item'),
    # url(r'^api/post/(?P<post_id>[0-9]+)/images/$', api_views.save_images, name='save_images'),  # todo
    # url(r'^api/user/(?P<user_id>[0-9]+)/profile/image/$', api_views.save_profile_image, name='save_profile_image'),  # todo
    # url(r'^api/post/(?P<post_id>[0-9]+)/$', api_views.update_post, name='update_post'),  # todo
    # url(r'^api/post/(?P<post_id>[0-9]+)/$', api_views.delete_post, name='delete_post'),  # todo
    # url(r'^api/user/(?P<user_id>[0-9]+)/profile/$', api_views.edit_profile, name='edit_profile'),  # todo
]
