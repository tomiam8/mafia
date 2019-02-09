from bottle import route, run, template, static_file, request, abort
from bottle.ext.websocket import GeventWebSocketServer
from bottle.ext.websocket import websocket
from threading import Thread

from os import path #probably bad practice but it's literally one line so I feel worse importing all of OS

fileRoot=path.dirname(__file__)

#STATIC ROUTES
@route('/site/<filepath:path>')
def serve_static(filepath):
    return static_file("/site/" + filepath, root=fileRoot)

#PAGE ROUTES
@route('/')
def serve_index():
    return serve_static("index.html")

@route('/play')
def serve_play():
    return serve_static("play.html")

#WEB SOCKET
@route('/websocket')
def handle_websocket():
    wsock = request.environ.get('wsgi.websocket') #create global websocket
    if not wsock:
        abort(400, 'Expected WebSocket request.')
    while True: #Yeah I know a while True... I didn't want to do it but every guide/tutorial I could find did it so??? Sorry.
        msg = wsock.receive()
        if msg is not None:
            wsock.send(msg)
            print(wsock)

#run(host='localhost', port=8080, debug=True, reloader=True)
run(host='localhost', port=8080, server=GeventWebSocketServer, reloader=True, debug=True) #Server that does Websockets