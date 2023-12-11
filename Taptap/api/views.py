from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth import authenticate
from rest_framework.status import HTTP_401_UNAUTHORIZED
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from datetime import datetime
from api.serializers import *


@api_view(['POST'])
def create_user(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        token, _ = Token.objects.get_or_create(user=user)
        return Response({'message': 'User created', 'error': False, 'token': token.key, 'user_id': user.pk, 'username': user.username})
    else:
        data = {'error': True, 'message': serializer.errors}
        return Response(data)


@api_view(["POST"])
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")

    user = authenticate(username=username, password=password)
    if user is None:
        return Response({'error': True, 'message': "Login failed"}, status=HTTP_401_UNAUTHORIZED)

    token, _ = Token.objects.get_or_create(user=user)
    return Response({"token": token.key, 'user_id': user.pk, 'username': user.username, 'error': False})


"""@api_view(['POST'])
def update_profile(request, user_id):
    user = User.objects.get(pk=user_id)
    user.profile.bio = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit...'
    user.save()
"""


@api_view(["GET"])
def countries(request):
    countries_list = Country.objects.all().order_by('id')
    serializer = CountrySerializer(countries_list, many=True)
    return Response(serializer.data)


@api_view(["GET"])
@permission_classes((IsAuthenticated,))
def regions(request):
    regions_list = Region.objects.all().order_by('id')
    serializer = RegionSerializer(regions_list, many=True)
    return Response(serializer.data)


@api_view(["GET"])
#@permission_classes((IsAuthenticated,))
def user_posts(request, user_id):
    page = request.GET.get('page', 1)
    posts = Post.objects.filter(user__pk=user_id)
    paginator = Paginator(posts, 50)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def post_hitcount(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    post.hitcount += 1
    post.save()
    return Response({'hitcount': post.hitcount})


@api_view(["GET"])
def posts(request, post_type):
    if post_type == 0:
        posts_list = Post.objects.order_by('-created_at')[:1000]
    else:
        posts_list = Post.objects.filter(type=post_type).order_by('-created_at')[:1000]
    page = request.GET.get('page', 1)
    paginator = Paginator(posts_list, 50)

    try:
        posts_list = paginator.page(page)
    except PageNotAnInteger:
        posts_list = paginator.page(1)
    except EmptyPage:
        posts_list = None  #paginator.page(paginator.num_pages)

    serializer = PostSerializer(posts_list, many=True)
    return Response({'error': False, 'posts': serializer.data})


@api_view(["POST"])
def search_post(request):
    data = request.data
    if data.get('type') == 0:  # search in all posts
        posts_list = Post.objects.filter(title__icontains=data.get('title')).order_by('-created_at')[:1000]
    else:
        posts_list = Post.objects.filter(**data.get('kwargs')).order_by('-created_at')[:1000]

    page = request.GET.get('page', 1)
    paginator = Paginator(posts_list, 50)

    try:
        posts_list = paginator.page(page)
    except PageNotAnInteger:
        posts_list = paginator.page(1)
    except EmptyPage:
        posts_list = paginator.page(paginator.num_pages)

    serializer = PostSerializer(posts_list, many=True)
    return Response(serializer.data)


@api_view(["POST"])
@permission_classes((IsAuthenticated,))
def create_post(request):
    serializer = PostSerializer(data=request.data)
    if serializer.is_valid():
        post = serializer.save()
        return Response({'message': 'Post created', 'error': False, 'id': post.id})
    else:
        data = {'error': True, 'message': serializer.errors}
        return Response(data)


@api_view(["GET"])
def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    serializer = PostSerializer(post)
    return Response(serializer.data)





