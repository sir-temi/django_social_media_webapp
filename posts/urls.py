from django.urls import path, include
from .  import views

app_name = 'posts'

urlpatterns = [
    path('', views.PostList.as_view(), name='list'),
    path('<username>/<int:pk>/', views.PostDetail.as_view(), name='single'),
    path('newpost/', views.CreatePost.as_view(), name='create'),
    path('delete/<pk>', views.DeletePost.as_view(), name='deletepost'),
    path('myposts/',views.UserPosts.as_view(),name='userposts'),
    path('posts-by-<username>/', views.OtherUserPost.as_view(),name='otherposts')
]