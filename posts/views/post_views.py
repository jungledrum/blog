from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from django.template import Context
from bson.objectid import ObjectId
from pymongo import MongoClient


db = MongoClient().blog


def index(req):
    posts = db.posts.find().sort('_id', -1)
    context = Context({'posts': posts})
    return render(req, 'posts/index.html', context)


def show(req, id):
    post = db.posts.find_one({'_id': ObjectId(id)})
    comments = db.comments.find({'post_id': id})
    context = Context({'post': post, 'comments': comments})
    return render(req, 'posts/show.html', context)


def new(req):
    categories = db.categories.find()
    return render(req, 'posts/new.html', {'categories': categories})


def create(req):
    title = req.POST['title']
    content = req.POST['content']
    category = req.POST['category']
    post = {'title': title, 'content': content, 'category': category}
    db.posts.insert(post)
    return redirect(reverse('posts.views.post_views.index'))


def edit(req, id):
    post = db.posts.find_one({'_id': ObjectId(id)})
    categories = db.categories.find()
    context = Context({'post': post, 'categories': categories})
    return render(req, 'posts/edit.html', context)


def update(req, id):
    title = req.POST['title']
    content = req.POST['content']
    category = req.POST['category']
    db.posts.update({'_id': ObjectId(id)},
                    {'$set': {'title': title, 'content': content, 'category': category}})
    return redirect(reverse('posts.views.post_views.show', args=(id,)))


def destroy(req, id):
    db.posts.remove({'_id': ObjectId(id)})
    return redirect(reverse('posts.views.post_views.index'))
    