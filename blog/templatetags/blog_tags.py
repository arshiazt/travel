from django import template
from ..models import Post,Comment,Category

register = template.Library()

@register.simple_tag(name='comment_count')
def function(pid):
    return Comment.objects.filter(post=pid,approved=True).count()

@register.inclusion_tag('blog/blog-category.html')
def post_category():

    posts = Post.objects.filter(status=1)
    category = Category.objects.all()
    cat_dict = {}
    
    for name in category:
        cat_dict[name] = posts.filter(category=name).count()
    return {'categories':cat_dict}

@register.inclusion_tag('blog/blog-latest-post.html')
def latest_post(arg=3):

    posts  = Post.objects.filter(status=1)[:arg]
    return {'posts':posts}