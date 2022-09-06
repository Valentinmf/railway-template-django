from django.urls import path
from blog.views import BlogHome, BlogPostDetail

app_name = "blog"

urlpatterns = [
    path('', BlogHome.as_view(), name='home'),
    path('<str:slug>/', BlogPostDetail.as_view(), name='blog'),
    ]