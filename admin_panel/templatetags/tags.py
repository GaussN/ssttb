from django import template

register = template.Library()


@register.simple_tag
def get_verbose_name(model):
    return model._meta.verbose_name


@register.simple_tag
def get_attr(obj, name):
    return getattr(obj, name)
