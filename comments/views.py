from django.shortcuts import render, redirect
from blogs.models import Blog
from comments.models import Comment
from profiles.models import Profile
# Create your views here.
def create_comment(request):
    if request.method == 'POST':
        
        profile = Profile.objects.get(user = request.user)
        blog_id = request.POST['blog_id']
        text = request.POST['comment']

        
        blog = Blog.objects.get(id = str(blog_id))
        
        comment = Comment()
        comment.text = text
        comment.author = profile
        comment.save()

        blog.comments.add(comment)
        blog.save


        return redirect('blogs:blog',blog_id=blog_id)
        