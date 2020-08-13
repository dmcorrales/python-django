from django import template
import markdown2
from courses.models import Course
from django.utils.safestring import mark_safe

register = template.Library()

@register.simple_tag
def last_course():
    '''Obtiene el último curso'''
    return Course.objects.latest('created_at')

@register.filter('time_estimate')
def time_estimate(word_count):
    '''Determina el tiempo estimado para lectura'''
    minutes = round(word_count/20)
    return minutes

@register.filter('markdown_to_html')
def markdown_to_html(markdown_text):
    '''Convierte markdown en html'''
    html_body = markdown2.markdown(markdown_text)
    return mark_safe(html_body)
