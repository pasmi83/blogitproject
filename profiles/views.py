from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from profiles.models import Profile
from django.contrib.auth.models import User
from django.contrib import messages #сообщения

# Create your views here.
@login_required
def user_profile_page(request,username):
    user = User.objects.get(username=username)
    profile = Profile.objects.get(user = user)
    context = {'profile':profile}
    return render(request,'profiles/profile.html',context=context)

@login_required
def user_profile_edit_page(request,username):
    user = User.objects.get(username=username)
    profile = Profile.objects.get(user = user)
    context = {'profile':profile}
    if request.method == 'GET':
        return render(request,'profiles/profile_edit.html',context=context)
    if request.method =='POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        status = request.POST['status']
        about = request.POST['about']

        user.first_name=first_name
        user.last_name=last_name
        user.email=email
        user.save()

        profile.status=status
        profile.about=about

        try:
            if any(request.FILES):
                profile.profile_image = request.FILES['profile_image']
        except:
            messages.error(reguest,'Profile Image is not correct!')
            return render(request,'profiles/profile_edit.html',context = context)
        profile.save()
        messages.success(request, 'Profile successfuly changed!')
        return redirect('/profile/{}'.format(user.username))
