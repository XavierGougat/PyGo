from django import template
from django.utils.html import escape

register = template.Library()

@register.filter(is_safe=True)
def citation(texte):   
    return "&laquo; {} &raquo;".format(escape(texte))
