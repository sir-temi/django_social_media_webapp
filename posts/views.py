from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, FormView, TemplateView
from django.urls import reverse, reverse_lazy
from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from . import models
from groups.models import Group
from .  import forms
from django.contrib.auth import get_user_model
User = get_user_model()

from braces.views import SelectRelatedMixin

class PostList(SelectRelatedMixin, ListView):
    model = models.Post
    select_related = ('user','group')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['groups'] = Group.objects.filter(members__username=self.request.user.username).order_by('-pk')
        context['other_groups'] = Group.objects.all().order_by('-pk')
        return context

class PostDetail(SelectRelatedMixin, DetailView):
    model = models.Post
    select_related = ('user','group')

class UserPosts(ListView):
    model = models.Post
    select_related = ('user','group')
    template_name = 'posts/user_post_list.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)

class OtherUserPost(ListView):
    select_related = ('user','group')
    template_name = 'posts/other_user_post.html'
    model = models.Post
    # def get_queryset(self):
    #     self.post = get_object_or_404(models.Post, user=User.objects.get(username=self.kwargs['username']))
    #     return models.Post.objects.filter(user=self.post)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post_list'] = models.Post.objects.filter(user__username = self.kwargs['username'])
        return context

class CreatePost(LoginRequiredMixin, SelectRelatedMixin, CreateView):
    model = models.Post
    fields = ('message', 'group')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class DeletePost(LoginRequiredMixin, DeleteView):
    model = models.Post
    success_url = reverse_lazy('posts:list')
    select_related = ('user','group')
    success_message = "Post Deleted"

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)