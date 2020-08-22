from django.shortcuts import render, redirect
from leads.forms import LeadForm
from leads.models import Lead
from django.contrib import messages
import json
from django.http import HttpResponse
from django.contrib.admin.views.decorators import staff_member_required

from django.core.mail import send_mail
from blogitproject.settings import EMAIL_HOST_USER

def contact_page(request):
    if request.method == 'POST':
        form = LeadForm(request.POST)
        if form.is_valid():
            name = request.POST.get('name', '')
            subject = request.POST.get('subject', '')
            message = request.POST.get('message', '')
            email = request.POST.get('email', '')
            new_lead = Lead.objects.create(
                name=name,
                subject=subject,
                message=message,
                email=email
            )
            new_lead.save()
            messages.success(request, '{}, your message successfully sent!'.format(new_lead.name))
        else:
            messages.error(request, "Something is going wrong...")
            
    
    form = LeadForm()

    context = {
        'form': form
    }
    return render(request, 'leads/contact.html', context=context)
