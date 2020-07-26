from django import template
from Car.models import Manufacturer

register = template.Library()


@register.inclusion_tag('Car/menu_tpl.html')
def show_menu(menu_class='menu'):
    manufacturers = Manufacturer.objects.all()
    return {"manufacturers": manufacturers, "menu_class": menu_class}
