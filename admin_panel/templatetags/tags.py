from django import template

register = template.Library()


@register.simple_tag
def get_model_name(model):
    return model.__class__.__name__


@register.simple_tag
def get_fields(model):
    return model._meta.fields


@register.simple_tag
def get_verbose_name(field):
    return field.verbose_name


@register.simple_tag
def get_name(field):
    return field.name


@register.simple_tag
def get_attr(obj, name):
    return getattr(obj, name)
