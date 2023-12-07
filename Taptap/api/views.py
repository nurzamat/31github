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






