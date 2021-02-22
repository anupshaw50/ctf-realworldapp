from gevent.pywsgi import WSGIServer
from project import app
import sys
from werkzeug.debug import DebuggedApplication

http_server = WSGIServer(('', int(sys.argv[1])),DebuggedApplication(app))
http_server.serve_forever()
