from django import template
from django.contrib.auth.models import User

register = template.Library()


@register.simple_tag(name='my_tag')
def calculate_number_of_user():
    user = User.objects.count()
    return user
