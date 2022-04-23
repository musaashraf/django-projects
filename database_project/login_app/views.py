from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.
from login_app.forms import UserForm, UserInfoForm
from login_app.models import UserInfo
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.urls import reverse


def index(request):
    diction = {}
    if request.user.is_authenticated:
        current_user = request.user
        user_id = current_user.id
        print(current_user.username)
        print(current_user.id)
        user_basic_info = User.objects.get(pk=user_id)
        user_more_info = UserInfo.objects.get(user__pk=user_id)
        #user_more_info = UserInfo.objects.filter(user=current_user).get()
        diction = {'user_basic_info': user_basic_info, 'user_more_info': user_more_info}
    return render(request, 'loginapp/index.html', context=diction)


def login_page(request):
    diction = {}
    return render(request, 'loginapp/login.html', context=diction)


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                # return HttpResponseRedirect(reverse('loginapp:index'))  //directpage
                # return render(request, 'loginapp/index.html')
                return index(request)
            else:
                return HttpResponse("Account is not active!!")
        else:
            return HttpResponse("Login Details are Wrong!")
    else:
        return render(request, 'loginapp/login.html', context={})


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('loginapp:index'))


def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        user_info_form = UserInfoForm(data=request.POST)

        if user_form.is_valid() and user_info_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            user_info = user_info_form.save(commit=False)
            user_info.user = user

            if 'profile_pic' in request.FILES:
                user_info.profile_pic = request.FILES['profile_pic']

            user_info.save()
            registered = True

    else:
        user_form = UserForm()
        user_info_form = UserInfoForm()

    diction = {'user_form': user_form, 'user_info_form': user_info_form, 'registered': registered}
    return render(request, 'loginapp/register.html', context=diction)
