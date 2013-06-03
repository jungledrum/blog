from django import template
from django.template import RequestContext
from django.template.loader import get_template
from pymongo import MongoClient
from bson.objectid import ObjectId


register = template.Library()
db = MongoClient().blog


@register.simple_tag(takes_context=True)
def show_category(context):
    t = get_template('category.html')
    categories = db.categories.find()
    c = RequestContext(context['request'], {'categories': categories})
    return t.render(c)


@register.simple_tag(takes_context=True)
def show_comments(context):
    t = get_template('comment.html')
    comments = db.comments.find().sort('_id', -1).limit(5)
    new_comments = []
    for comment in comments:
        post = db.posts.find_one({'_id': ObjectId(comment['post_id'])})        
        comment['post_title'] = post['title']
        new_comments.append(comment)
    c = RequestContext(context['request'], {'comments': new_comments})
    return t.render(c)
