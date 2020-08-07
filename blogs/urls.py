from django.urls import path
from . import views
from comments.views import create_comment
app_name = 'blogs'
urlpatterns = [
    path('<int:blog_id>',views.blog, name='blog'),
    path('create',create_comment, name = 'create_comment'),
    path('add-or-remove-like-ajax',views.add_or_remove_like_ajax, name = 'add_or_remove_like_ajax'),
    ]

