from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth import logout
from django.contrib.auth.models import User
from profiles.models import Profile
from django.contrib import messages #сообщения

# Create your views here.

def login(request):
    context={}
    if request.method == 'GET':
        return render(request,'accounts/login.html',context=context)
    if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(request, username = username, password = password)
            if user is not None:
                auth.login(request, user)
                messages.success(request, 'Welcome back, {}!'.format(user.username))#сообщения
                return redirect('pages:index')
            else:
                messages.error(request,'Username or password is incorrect')
                return render(request,'accounts/login.html',context=context)
def register(request):
    context={}
    if request.method == 'GET':
        return render(request,'accounts/register.html', context=context)
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        password1 = request.POST['password1']
        if password == password1:
            try:
                user = User.objects.create_user(
                    username=username,
                    password=password,
                    email=email,
                    first_name=first_name,
                    last_name=last_name
                )
                #profile = Profile() #функционал вынесен в profile.models
                #profile.user = user
                #profile.save()
                
                
                #return redirect('pages:index')
            except:
                messages.error(request, 'Somthing going wrong... Please, try again...')
                return render(request, 'accounts/register.html', context=context)
            else:
                auth.login(request, user)
                messages.success(request, '{}, you have been registered successfuly! Fill your profile details now or you can do it later!'.format(user.username))
                return redirect('pages:index')
        else:
            messages.error(request, 'Password and Confirm Password is not match... Please,try again')
            return render(request, 'accounts/register.html', context=context)

                



def logout(request):
    auth.logout(request)
    return redirect('pages:index')


