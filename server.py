from bottle import route, run, template, static_file
import os

fileRoot=os.path.dirname(__file__)

#STATIC ROUTES
@route('/static/<filepath:path>')
def server_static(filepath):
    return static_file("/static/" + filepath, root=fileRoot)

#PAGE ROUTES
@route('/')
def root():
    return static_file("/page/index.html", root=fileRoot)

run(host='localhost', port=8080, debug=True, reloader=True)