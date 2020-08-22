from django.urls import path
from . import views
from comments.views import create_comment
app_name = 'leads'
urlpatterns = [
    path('',views.contact_page, name='leads'),
    ]

