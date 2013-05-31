from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from django.template import Context
from bson.objectid import ObjectId
from pymongo import MongoClient


db = MongoClient().blog


def index(req):
    categories = db.categories.find().sort('_id', -1)
    context = Context({'categories': categories})
    return render(req, 'categories/index.html', context)

def show(req, name):
    posts = db.posts.find({'category': name})
    return render(req, 'categories/show.html', {'posts': posts})


def create(req):
    name = req.POST['name']
    category = {'name': name}
    db.categories.insert(category)
    return redirect(reverse('posts.views.category_views.index'))