from django import template


register = template.Library()


@register.filter
def perc(value):
    return f"{value:.2%}"