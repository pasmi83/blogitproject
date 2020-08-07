
from django.shortcuts import render
from blogs.models import Blog
from comments.models import Comment
import json
from django.http import HttpResponse 
# Create your views here.
def blog(request,blog_id):
    
    if request.method == "GET":
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
        'blog':blog,
        'like_class':like_class,
        'like_color':like_color,
        'font_size':font_size,
               }
        return render(request, 'blogs/blog.html', context = context)
# добавление или снятие лайков
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

    