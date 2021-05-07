from django.contrib import admin
from . import models
# Register your models here.

# this lets you view this child model which is a foreign key to Group in the group admin page
# class GroupMemberInline(admin.TabularInline):
#     model = models.GroupMember

admin.site.register(models.Group)

