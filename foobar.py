# -*- coding: utf-8 -*-

import os
import bottle
from bottle import route, view, request, abort, error
from lib.pagination import paginate
from models import Category, Post


bottle.TEMPLATE_PATH.append('./templates/')
STATIC_ROOT = os.path.join(os.path.dirname(__file__), 'public', 'static')

def add_categories(func):
    """ Adds category list to each func output """
    def wrapper(*args, **kwargs):
        output = func(*args, **kwargs)
        if not isinstance(output, dict):
            return output
        output.update({'categories': Category.objects().all()})
        return output
    return wrapper


@route('/')
@view('index')
@add_categories
def index():
    """ Index page controller """
    paginator = paginate(request, Post.objects().filter_by(is_published=True))
    
    return {'paginator': paginator}


@route('/category/:slug#[\w-]+#')
@view('category')
@add_categories
def category(slug):
    """ Category page controller """
    category = Category.objects().filter_by(slug=slug).first()
    if not post:
        abort(404)
    paginator = paginate(request, Post.objects().filter_by(is_published=True, 
                                                           category_id=category.id))

    return {'category': category, 'paginator': paginator}


@route('/post/:slug#[\w-]+#')
@view('post')
@add_categories
def post(slug):
    """ Single post controller """
    post = Post.objects().filter_by(slug=slug, is_published=True).first()
    if not post:
        abort(404)
    return {'post': post}


@error(404)
def error404(error):
    """ Error 404 """
    return u'Страница не найдена.'
