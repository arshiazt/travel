from django import template
from ..models import Post,Comment,Category

register = template.Library()

@register.simple_tag(name='comment_count')
def function(pid):
    return Comment.objects.filter(post=pid,approved=True).count()