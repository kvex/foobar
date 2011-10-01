# -*- coding: utf-8 -*-

from foobar import *
from bottle import static_file


# static files
@route('/static/img/:filename#.*\.(jpg|png|gif)#')
def send_image(filename):
    type = filename.split('.')[-1]
    
    return static_file(filename, root=os.path.join(STATIC_ROOT, 'img'), 
                       mimetype='image/%s' % type)

@route('/static/css/:filename#.*\.css#')
def send_css(filename):
    return static_file(filename, root=os.path.join(STATIC_ROOT, 'css'))

@route('/static/js/:filename#.*\.js#')
def send_js(filename):
    return static_file(filename, root=os.path.join(STATIC_ROOT, 'js'))

# logging
import logging
logging.basicConfig()
logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)

# debug & dev server
bottle.debug(True)
bottle.run(host='localhost', port=8080, reloader=True)
