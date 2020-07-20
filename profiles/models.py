from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from profiles.utils import generate_profile_thumbnail
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=150, blank=True, default='')
    about = models.TextField(default='', blank=True)
    profile_image = models.ImageField(upload_to='profile_image/%Y/%m/%d',
                                     default='default/default_profile_image.png',
                                    verbose_name='Profile Image',
                                   blank=True)
    profile_image_thumbnail = models.ImageField(upload_to='profile_image_thumbnail/%Y/%m/%d', 
                                                blank=True, verbose_name='Profile Image Thumbnail')
   
    def __str__(self):
        return self.user.get_full_name()

    def delete(self, *args, **kwargs):
        if self.profile_image.name.split('/')[-1] != 'default_profile_image.png':
            self.profile_image.delete(save=False)
            self.profile_image_thumbnail.delete(save=False)
        super().delete(*args, **kwargs)
    
    def save(self, *args, **kwargs):
        self.profile_image_thumbnail = generate_profile_thumbnail(self.id,
                                                                 self.profile_image, 200, 200)
        super(Profile, self).save(*args, **kwargs)

    
    
    
    

@receiver(post_save,sender=User)
def create_user_profile(sender,instance,created,*args,**kwargs):
    if created:
        profile=Profile()
        profile.user = instance
        profile.save()