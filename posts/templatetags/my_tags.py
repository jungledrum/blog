from django import template
from django.template import Context
from django.template.loader import get_template
from pymongo import MongoClient


register = template.Library()
db = MongoClient().blog


@register.simple_tag
def show_category():
    t = get_template('category.html')
    categories = db.categories.find()
    c = Context({'categories': categories})
    return t.render(c)
