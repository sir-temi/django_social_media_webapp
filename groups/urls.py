from django.urls import path, include
from . import views

app_name = 'groups'
urlpatterns = [
    path('create/', views.CreateGroup.as_view(), name='create'),
    path('<slug>/', views.SingleGroup.as_view(), name='single'),
    path('', views.ListGroups.as_view(), name='groupslist'),
    path('join/<slug>/', views.JoinGroup.as_view(), name='joingroup'),
    path('leave/<slug>/', views.LeaveGroup.as_view(), name='leavegroup'),
]