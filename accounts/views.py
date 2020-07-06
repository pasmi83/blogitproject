from django.shortcuts import render, redirect
from django.contrib import auth

# Create your views here.

def login(request):
    if request.method == 'GET':
        context={}
        return render(request,'accounts/login.html',context=context)
    if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(request, username = username, password = password)
            if user is not None:
                auth.login(request, user)
                return redirect('pages:index')
            else:
                return render(request,'accounts/login.html',context=context)
def register(request):
    context={}
    return render(request,'accounts/register.html', context=context)