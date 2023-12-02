from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.db import IntegrityError, transaction
from .models import UserProfile


def index(request):
    return render(request, 'account/login.html')


def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('account:home')
        else:
            return render(request, 'account/login.html', {'alert': "Неверный логин или пароль"})
    else:
        return render(request, 'account/login.html')


def signup(request):
    if request.method == "POST":
        email_phone = request.POST.get('email_phone')
        username = request.POST.get('username')
        password = request.POST.get('user_password')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        middle_name = request.POST.get('middle_name')
        city = request.POST.get('city')
        country = request.POST.get('country')
        address = request.POST.get('address')

        if '@' in email_phone:
            email = email_phone
            phone = ''
        else:
            email = ''
            phone = email_phone

        username_exists = User.objects.filter(username__iexact=username).exists()
        if username_exists:
            return render(request, 'account/signup.html', {'alert': "Такой логин существует в системе",
                                                           'username': username})

        try:
            with transaction.atomic():
                user_profile, user = save_registration(address, city, country, username, email, first_name, last_name, middle_name, password, phone)
        except IntegrityError:
            return render(request, 'account/signup.html', {'alert': "Ошибка при регистрации",
                                                           'username': username})

        if user and user_profile:
            login(request, user)
            return redirect('account:home')
        else:
            return render(request, 'account/signup.html', {'alert': "Ошибка регистрации",
                                                           'username': username})
    else:
        return render(request, 'account/signup.html')


def save_registration(address, city, country, username, email, first_name, last_name, middle_name, password, phone):

    user = User(username=username, email=email, first_name=first_name, last_name=last_name, is_staff=1)
    user.set_password(password)
    user.save()
    user_profile = UserProfile.objects.create(user=user, address=address, country=country, city=city,
                                              middle_name=middle_name, phone=phone)

    return user_profile, user


def validate_username_ajax(request):
    username = request.GET.get('username', None)
    data = {
        'is_taken': User.objects.filter(username__iexact=username).exists()
    }
    if data['is_taken']:
        data['error_message'] = 'Такой логин существует в системе'
    return JsonResponse(data)


@login_required
def user_logout(request):
    logout(request)
    return redirect('account:user_login')


@login_required
def home(request):
    user = request.user
    return render(request, 'account/home.html', {'profile': user.userprofile, 'user': user})


@login_required
def profile(request):
    user = request.user
    return render(request, 'account/profile.html', {'profile': user.userprofile, 'user': user})

