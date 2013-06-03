from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from django.template import Context
from bson.objectid import ObjectId
from pymongo import MongoClient


db = MongoClient().blog

def new(req):
    return render(req, 'new.html', {})

def login(req):
    username = req.POST['username']
    password = req.POST['password']
    if username == 'bo' and password == 'bo':
        req.session['username'] = 'bo'
        return redirect(reverse('posts.views.post_views.index'))
    else:
        return redirect(reverse('admin.views.new'))

def logout(req):
    del req.session['username']
    return redirect(reverse('posts.views.post_views.index'))