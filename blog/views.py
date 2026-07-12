from django.shortcuts import render,get_object_or_404
from .models import Post,Comment
from .forms import CommentForm

# Create your views here.

def blog_view(request,**kwargs):

    posts = Post.objects.filter(status=1)
    if kwargs.get('cat_name') != None:
        posts = posts.filter(category__name=kwargs['cat_name'])
    if kwargs.get('author_username') != None:
        posts = posts.filter(author__username=kwargs['author_username'])
    if kwargs.get('tag_name') != None:
        posts = posts.filter(tags__name__in=[kwargs['tag_name']])

    context = {'posts':posts}
    return render(request,'blog/blog-home.html',context)

def blog_single_view(request):
    return render(request,'blog/blog-single.html')