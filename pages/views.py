from django.shortcuts import render
from blogs.models import Blog
from .utils import order_list_generator #список параметров для сортировки
from django.contrib import messages #сообщения
from django.core.paginator import Paginator #класс-пагинатор

# Create your views here.
def index(request):
    #сортировка по
    order = request.GET.get('order_by','')
    blogs = Blog.objects.order_by(*order_list_generator(order))
    #-------------------------------------------------------------

    #последние 5 сообщений
    if order != '-created_at':
        recent_posts = blogs.order_by('-created_at')[:5]
    else:
        recent_posts=blogs[:5]
    #-------------------------------------------------------------

    #поиск по содержимому
    search = request.GET.get('searching','')
    if search:
        blogs = blogs.filter(text__icontains = search)
    #-------------------------------------------------------------------
    
    #фильтрация по тегам
    tag_cloud = Blog.tags.all()
    filter_tag = request.GET.get('tag','')
        
    if filter_tag:
        blogs = blogs.filter(tags__name__icontains = filter_tag)
        if  not blogs:
            messages.error(request,"You have no blogs with these tags!")
    #--------------------------------------------------------------------
    #пагинация
    paginator = Paginator(blogs,3)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
   
    #--------------------------------------------------------------------   
    print ('!!!!',blogs.model)
    print ('2!!!',blogs.__class__.__name__)
    context = {
        'blogs':blogs,
        'recent_posts':recent_posts,
        'tag_cloud':tag_cloud,
        'page':page,
               }
    return render(request, 'pages/index.html', context = context)