from django.urls import path
from . import views
app_name = 'profiles'
urlpatterns = [
    path('<slug:username>/',views.user_profile_page, name='user_profile_page'),
    path('<slug:username>/edit/',views.user_profile_edit_page, name='user_profile_edit_page'),
    ]
