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

@staff_member_required
def send_answer(request, lead_id):
    try:
        lead = Lead.objects.get(id=str(lead_id))
    except:
        return redirect('/admin/leads/lead/')

    if request.is_ajax():
        answer = request.POST.get('answer', '')
        user = request.user
        answer_status = False
        if not lead.is_email_answer_send and answer:
            lead.answer = answer
            lead.answered_by = user
            lead.is_email_answer_send = True
            lead.save()
            send_mail(
                subject='Ответ на ' + lead.subject,
                message='Добрый день, {0}!\n{1}'.format(lead.name, lead.answer),
                from_email=EMAIL_HOST_USER,
                recipient_list=[lead.email],
                fail_silently=False,
            )
            answer_status = True

        return HttpResponse(json.dumps({'answer_status': answer_status}), content_type='application/json')