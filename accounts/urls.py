from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views


app_name = 'accounts'

urlpatterns = [
    path('login', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout', auth_views.LogoutView.as_view(next_page='thanks'), name='logout'),
    path('register', views.UserSignUpView.as_view(), name='register'),
    path('dashboard/', views.Dashbaord.as_view(), name='dashboard')
]