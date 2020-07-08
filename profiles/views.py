from django.shortcuts import render
# Create your views here.
def profile(request):
    content = {}
    return render('profiles/profile.html',content=content)