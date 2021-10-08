from django import template

register = template.Library()


@register.filter
def split_by_comma(value):
    """Divide a string by ','"""
    return value.split(",")

