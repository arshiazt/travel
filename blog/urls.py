from django.urls import path
from .views import blog_view,blog_single_view

app_name = 'blog'

urlpatterns = [
    path('',blog_view,name='index'),
    path('single',blog_single_view,name='single'),
]
