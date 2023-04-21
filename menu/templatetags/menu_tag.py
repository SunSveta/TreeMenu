from menu.models import MenuCategories
from django import template

register = template.Library()


@register.simple_tag()
def draw_menu(path):
    result = MenuCategories.objects.select_related('parent').filter(link=path, parent=None) \
        .prefetch_related('child_item').prefetch_related('child_item')

    return result
