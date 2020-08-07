from django.shortcuts import render
from blogs.models import Blog

# Create your views here.
def index(request):
    blogs = Blog.objects.all()
    context = {
        'blogs':blogs       
               }
    return render(request, 'pages/index.html', context = context)