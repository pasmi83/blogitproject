from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, reverse
from blogs.models import Blog
from comments.models import Comment
import json
from django.http import HttpResponse
from django.contrib import messages #сообщения
# Create your views here.
def blog(request,blog_id):
    
    if request.method == "GET":
        #recent_posts = Blog.by_date.all()[:5]
        blog = Blog.objects.get(id=blog_id)
        if str(request.user.profile.id) in blog.likes:
            like_class = "fa fa-heart"
            like_color = "red"
            font_size = "14px"
        else:
            like_class = "fa fa-heart-o"
            like_color = "grey"
            font_size = "18px"

        comments = Comment.objects.all()
        context = {
        #'recent_posts':recent_posts,
        'blog':blog,
        'like_class':like_class,
        'like_color':like_color,
        'font_size':font_size,
               }
        return render(request, 'blogs/blog.html', context = context)
# добавление или снятие лайков
@login_required
def add_or_remove_like_ajax(request):
    if request.is_ajax():
        blog_id = request.POST['blog_id']
        print (f'blog_id: {blog_id} {type(blog_id)}')
        blog = Blog.objects.get(id=blog_id)
        current_profile_id = str(request.user.profile.id)
        print (f'current_profile_id: {current_profile_id},{type(current_profile_id)}')
        if current_profile_id in blog.likes:
            like_class = 'fa fa-heart-o'
            like_color = 'gray'
            like_font = '18px'
            blog.likes.remove(current_profile_id)
            
        else:
            like_class = 'fa fa-heart'
            like_color = 'red'
            like_font = '14px'
            blog.likes.append(current_profile_id)
        blog.save()
        
        return HttpResponse(json.dumps({'class':like_class,
                                        'color':like_color,
                                        'font':like_font,
                                       'likes':len(blog.likes)}),
                            content_type = 'application/json')
@login_required
def create_blog(request):
    if request.method =="GET":
        context = {}
        return render(request, 'blogs/create_blog.html', context = context)
    if request.method =="POST":
        blog = Blog()
        blog.author=request.user.profile
        blog.title=request.POST['title']
        blog.text=request.POST['text']
        #тэги
        tags = request.POST.get('tags').split(",")#делим строку из формы по запятым
        tags = [i.strip() for i in tags]#режем пробелы с обеих сторон
        #----------------------------------------------
        try:
            if any(request.FILES):
                blog.image = request.FILES['image']
        except:
            messages.error(reguest,'Image is not correct!')
            return redirect(reverse('pages:index'))
        blog.likes = []
        
        blog.save()
        blog.tags.set(*tags)#назначаем тэги в свежесохранённому блогу(или наоборот)
        
        messages.success(request, 'Blog successfuly created!')
        return redirect(reverse('pages:index'))
@login_required
def edit_blog(request,blog_id):


    blog = Blog.objects.get(id=blog_id)
    tags = ','.join(blog.tags.names())
    if blog.author == request.user.profile:
        
        if request.method == "GET":
            context = {'blog':blog,'tags':tags}
            return render(request,  'blogs/edit_blog.html',context = context )
        
        if request.method =="POST":
       
            blog.title=request.POST['title']
            blog.text=request.POST['text']
            
            #тэги
            tags = request.POST.get('tags').split(",")#делим строку из формы по запятым
            tags = [i.strip() for i in tags]#режем пробелы с обеих сторон
            #----------------------------------------------
            
            try:
                if any(request.FILES):
                    blog.image = request.FILES['image']
            except:
                messages.error(request,'Image is not correct!')
                return redirect(reverse('pages:index'))
            
            blog.save()
            blog.tags.set(*tags)
            messages.success(request, 'Blog successfuly edited!')
            return redirect('/blog/'+str(blog_id))
    else:
        messages.error(request,"It's not your blog")
        return redirect('/blog/'+str(blog_id))






