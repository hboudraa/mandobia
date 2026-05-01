from django import template

register = template.Library()


@register.filter
def abs_value(value):
    """
    Returns the absolute value of a number
    Usage: {{ value|abs_value }}
    """
    try:
        return abs(int(value))
    except (ValueError, TypeError):
        return value

