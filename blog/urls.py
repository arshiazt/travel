from django.urls import path
from .views import blog_view,blog_single_view

app_name = 'blog'

urlpatterns = [
    path('',blog_view,name='index'),
    path('single',blog_single_view,name='single'),
    path('category/<str:cat_name>' ,blog_view,name='category'),
    path('tag/<str:tag_name>' ,blog_view,name='tag'),
    path('author/<str:author_username>',blog_view,name='author'),
]
