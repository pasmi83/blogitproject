from django.db import models
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver
# from django.conf import settings
from blogitproject.settings import EMAIL_HOST_USER

class Lead(models.Model):
    name = models.CharField(max_length=60, blank=True, default='')
    subject = models.CharField(max_length=60, blank=True, default='')
    email = models.EmailField(max_length=250, blank=True, default='')
    message = models.TextField(blank=True, default='')
    created_at = models.DateTimeField(auto_now=True, blank=True)
    updated_at = models.DateTimeField(auto_now_add=True, blank=True)
    answer = models.TextField(blank=True, default='')
    is_email_answer_send = models.BooleanField(default=False)
    answered_by = models.ForeignKey(User, blank=True, on_delete=models.DO_NOTHING, null=True)
    notice = models.TextField(blank=True, default='')
     
    def __str__(self):
        return f'{self.mail} {self.subject} ({self.id})'
        
@receiver(post_save, sender=Lead)
def create_user_profile(sender, instance, created, *args, **kwargs):
    if created:
        subject = instance.subject
        message = instance.message + '\n from {0} with email {1}'.format(instance.name, instance.email)
        recipient_list = [u.email for u in User.objects.all() if u.is_staff]
        send_mail(
            subject=subject,
            message=message,
            from_email=EMAIL_HOST_USER,
            recipient_list=recipient_list,
            fail_silently=False,
            )