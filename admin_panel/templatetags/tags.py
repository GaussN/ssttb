from django import template

register = template.Library()


@register.simple_tag
def get_attr(obj, name):
    return getattr(obj, name)


@register.simple_tag
def get_attr_verbose_name_from_meta(meta, name):
    return meta.get_field(name).verbose_name
