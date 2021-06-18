from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, HttpResponseRedirect
from App_Login.forms import CreateNewUser
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse, reverse_lazy
from .models import UserProfile
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from App_Login.forms import EditProfile
from App_Post.forms import PostForm
from django.contrib.auth.models import User
# Create your views here.


def sign_up(request):
    form = CreateNewUser()
    registered = False
    if request.method == 'POST':
        form = CreateNewUser(data=request.POST)
        if form.is_valid():
            user = form.save()
            registered = True
            user_profile = UserProfile(user=user)
            user_profile.save()
            return HttpResponseRedirect(reverse('App_Login:login'))
    return render(request, 'App_Login/sign_up.html', context={'title': 'Sign up', 'form': form, 'registered': registered})


def login_page(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('home'))
    return render(request, 'App_Login/login.html', context={'title': 'Login', 'form': form})


@login_required
def edit_profile(request):
    profile = UserProfile.objects.get(user=request.user)
    form = EditProfile(instance=profile)
    if request.method == 'POST':
        form = EditProfile(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save(commit=True)
            #form = EditProfile(instance=profile)
            return HttpResponseRedirect(reverse('App_Login:profile'))
    return render(request, 'App_Login/profile.html', context={'form': form})


@login_required
def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('App_Login:login'))


@login_required
def user_profile(request):
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return HttpResponseRedirect(reverse('home'))
    return render(request, 'App_Login/user.html', context={'title': 'User', 'form': form})


def other_user(request, username):
    user_other = User.objects.get(username=username)
    if user_other == request.user:
        return HttpResponseRedirect(reverse('App_Login:profile'))
    return render(request, 'App_Login/other_user.html', context={'user_other': user_other})
