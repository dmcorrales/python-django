from django import template
from courses.models import Course

register = template.Library()

@register.simple_tag
def last_course():
    '''Obtiene el último cuero'''
    return Course.objects.latest('created_at')

