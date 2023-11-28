from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.db import IntegrityError, transaction


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
        inviter = request.POST.get('inviter')
        email_phone = request.POST.get('email_phone')
        tree_parent = request.POST.get('parent_id')
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

        if inviter == '':
            return render(request, 'account/signup.html', {'alert': "Регистрируйтесь по реферальной ссылке",
                                                           'inviter': inviter})

        username_exists = User.objects.filter(username__iexact=username).exists()
        if username_exists:
            return render(request, 'account/signup.html', {'alert': "Такой логин существует в системе",
                                                           'inviter': inviter})

        try:
            with transaction.atomic():
                user = save_registration(address, city, country, username, email, first_name, last_name, iddle_name, password, phone)
        except IntegrityError:
            return render(request, 'account/signup.html', {'alert': "Ошибка при регистрации",
                                                           'inviter': inviter})

        if user:
            login(request, user)
            return redirect('account:home')
        else:
            return render(request, 'account/signup.html', {'alert': "Ошибка регистрации",
                                                           'inviter': inviter})
    else:
        return render(request, 'account/signup.html')


def save_registration(address, city, country, username, email, first_name, last_name, middle_name, password, phone):

    user = User(username=username, email=email, first_name=first_name, last_name=last_name, is_staff=1)
    user.set_password(password)
    user.save()
    return user


