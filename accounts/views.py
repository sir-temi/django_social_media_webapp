from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, FormView, TemplateView
from .forms import UserSignUpForm
from django.urls import reverse, reverse_lazy
# Create your views here.

class UserSignUpView(CreateView):
    form_class = UserSignUpForm
    success_url = reverse_lazy('accounts:login')
    template_name = 'accounts/register.html'

class Dashbaord(TemplateView):
    template_name = 'dashboard.html'
