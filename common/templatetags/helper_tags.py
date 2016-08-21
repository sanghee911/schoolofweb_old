from django.template import Library
from django.conf import settings
import os

register = Library()


@register.simple_tag
def template_dir(this_object, its_name=""):
    if settings.DEBUG:
        output = dir(this_object)
        return "<pre>" + str(its_name) + " " + str(output) + "</pre>"
    return ""


@register.simple_tag
def replace_url(old_queries, new_queries):
    if old_queries:
        return '?%s&page=%s' % (old_queries, new_queries)
    else:
        return '?page=%s' % new_queries


@register.filter(name='addcss')
def addcss(field, css):
    return field.as_widget(attrs={"class": css})


@register.filter(name='has_permission_to_update')
def has_group(user):
    if user.is_superuser:
        return True
    valid_groups = ['staff', 'manager']
    for valid_group in valid_groups:
        if user.groups.filter(name=valid_group).exists():
            return True

    return False


@register.filter(name='base_filename')
def base_filename(value):
    return os.path.basename(value)


@register.filter(name='get_type')
def get_type(value):
    return type(value)
