from django.db import models
import misaka as m
from django.urls import reverse
from django.utils.text import slugify
from django.contrib.auth import get_user_model
User = get_user_model()

from django import template
register = template.Library()


class Group(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(allow_unicode=True, unique=True)
    description = models.TextField(blank=True)
    description_html = models.TextField(editable=False, blank=True)
    members = models.ManyToManyField(User, through='GroupMember')

    def __str__(self):
        return self.name

    def save(self,*args,**kwargs):
        self.description_html = m.html(self.description)
        self.slug = slugify(self.name,allow_unicode=True)
        super().save(*args,**kwargs)

    def get_absolute_url(self):
        return reverse('groups:single', kwargs={'slug': self.name})



class GroupMember(models.Model):
    group = models.ForeignKey(Group, related_name='memberships', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='user_groups', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

    class Meta:
        unique_together = ('group','user')


