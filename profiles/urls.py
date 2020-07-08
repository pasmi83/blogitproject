from django.urls import path
from . import views
app_name = 'profiles'
urlpatterns = [
    path('<slug:user>/',views.profile, name='profile'),
    ]
