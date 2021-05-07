from django.db import models
from django.conf import settings
import misaka
# Create your models here.
from groups.models import Group

from django.urls import reverse
from django.contrib.auth import get_user_model
User = get_user_model()

class Post(models.Model):
    user = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
    posted_at = models.DateTimeField(auto_now=True)
    message = models.TextField()
    message_html = models.TextField(editable=False)
    group = models.ForeignKey(Group, related_name='posts',null=True,blank=True,on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} {self.message}"

    def save(self,*args,**kwargs):
        self.message_html = misaka.html(self.message)
        super().save(*args,**kwargs)

    def get_absolute_url(self):
        return reverse('posts:single', kwargs={'pk': self.pk, 'username':self.user.username})

    class Meta:
        ordering = ['-posted_at']
        unique_together = ['user', 'message']