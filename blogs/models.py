from django.db import models
from profiles.models import Profile
from comments.models import Comment
from django.contrib.postgres.fields import ArrayField

class Blog(models.Model):
    title = models.CharField(max_length=250, blank=False, default = 'Without title.')
    text = models.TextField(default = '', blank = False)
    text_slug = models.CharField(default = '', blank = True, max_length=200)
    author = models.ForeignKey(to = Profile, on_delete = models.DO_NOTHING)
    image = models.ImageField(upload_to='blog_image/%Y/%m/%d', verbose_name='Главное изображение', blank = False)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    comments = models.ManyToManyField(Comment, blank = True)
    likes =  ArrayField(models.CharField(max_length = 30, blank = True, default = list))

    def save(self, *args, **kwargs):
        self.text_slug = self.text[:197]+'...'
        super(Blog, self).save(*args, **kwargs)