from django import template
from doggie.models import DogCategory

register = template.Library()

@register.inclusion_tag('doggie/dogcategories.html')
def get_dogcategory_list(current_dogcategory=None):
    return {'dogcategories': DogCategory.objects.all(),
            'current_dogcategory': current_dogcategory}
