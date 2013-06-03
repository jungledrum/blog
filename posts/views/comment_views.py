from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from django.template import Context
from bson.objectid import ObjectId
from pymongo import MongoClient
from posts.utils import login_required


db = MongoClient().blog

def index(req):
    pass

def create(req, post_id):
    name = req.POST['name']
    content = req.POST['content']
    comment = {'name': name, 'content': content, 'post_id': post_id}
    db.comments.insert(comment)
    return redirect(reverse('posts.views.post_views.show', args=(post_id,)))


@login_required
def destroy(req, post_id, comment_id):
    db.comments.remove({'_id': ObjectId(comment_id)})
    return redirect(reverse('posts.views.post_views.show' ,args=(post_id,)))
