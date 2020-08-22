from django.db import models
from django.contrib.auth.models import User

class Lead(models.Model):
    name = models.CharField(max_length = 60, blank = True, default = '')
    subject = models.CharField(max_length = 60, blank = True, default = '')
    email = models.EmailField(max_length = 250, blank = True, default = '')
    message = models.TextField(blank = True, default='')
    created_at = models.DateTimeField(auto_now=True, blank = True)
    uploated_at = models.DateTimeField(auto_now_add = True, blank = True)
    answer = models.TextField(blank=True,default='')
    is_email_answer_send = models.BooleanField(default = False)
    answerwd_by = models.ForeignKey(User,blank = True, on_delete = models.DO_NOTHING)
    notice = models.TextField(blank=True, default='')
     
    def __str__(self):
        return f'{self.mail} {self.subject} ({self.id})'
        
