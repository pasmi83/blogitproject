from django.urls import path
from . import views
from comments.views import create_comment
app_name = 'blogs'
urlpatterns = [
    path('<int:blog_id>',views.blog, name='blog'),
    path('comment',create_comment, name = 'create_comment'),
    path('create',views.create_blog, name = 'create_blog'),
    path('<int:blog_id>/edit',views.edit_blog, name = 'edit_blog'),
    path('add-or-remove-like-ajax',views.add_or_remove_like_ajax, name = 'add_or_remove_like_ajax'),
    ]

