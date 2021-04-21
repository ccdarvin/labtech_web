from django import template
from ..models import Menu
register = template.Library()


register = template.Library()


@register.simple_tag(takes_context=True)
def menu(context, code):
    request = context['request']
    menu = Menu.objects.filter(site=request._wagtail_site, code=code).first()
    return menu


@register.simple_tag(takes_context=True)
def root_site(context):
    request = context['request']
    return request._wagtail_site


@register.simple_tag(takes_context=True)
def root_page(context):
    request = context['request']
    return request._wagtail_site.root_page
