from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import ListView, RedirectView,DetailView, CreateView, UpdateView, DeleteView, FormView, TemplateView
from django.urls import reverse, reverse_lazy
from django.shortcuts import render, get_object_or_404, redirect
from .models import Group
from django.contrib import messages


class CreateGroup(LoginRequiredMixin, CreateView):
    fields = ('name','description')
    model = Group

class SingleGroup(DetailView):
    model = Group
    # slug_field = 'slug'

class ListGroups(ListView):
    model = Group


class JoinGroup(LoginRequiredMixin, RedirectView):
    
    # def get_redirect_url(self, *args, **kwargs):
    #     return redirect('groups:single', slug=slug)

    def get_redirect_url(self, *args, **kwargs):
        return reverse('groups:single', kwargs={'slug':self.kwargs.get('slug')})

    
    
    def get(self, request, *args, **kwargs):
        group = get_object_or_404(Group, slug=self.kwargs.get('slug'))
        try:
            group.members.add(self.request.user)
        except:
            messages.warning(request, 'You are already a member of this group')
        else:
            messages.success(request, 'You have successfully joined')
        return super().get(request, *args, **kwargs)

class LeaveGroup(LoginRequiredMixin, RedirectView):

    def get_redirect_url(self, *args, **kwargs):
         return reverse('groups:single', kwargs={'slug':self.kwargs.get('slug')})
        
    def get(self, request, *args, **kwargs):
        group = get_object_or_404(Group, slug=self.kwargs.get('slug'))
        try:
            group.members.remove(self.request.user)
        except:
            messages.warning(request, 'You are not a member of this group')
        else:
            messages.success(request, 'You have successfully left the group')
        return super().get(request, *args, **kwargs)