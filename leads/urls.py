from django.urls import path
from . import views

app_name = 'leads'
urlpatterns = [
    path('',views.contact_page, name='contact_page'),
    path('send_answer/<int:lead_id>', views.send_answer, name='send_answer'),
    ]

