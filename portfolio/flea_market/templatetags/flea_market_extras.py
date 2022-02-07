from django import template

register = template.Library()

@register.filter
def check_bookmark(value, product):
    return value.filter(ad=product).count()