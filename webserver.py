import os
from http.server import HTTPServer, CGIHTTPRequestHandler
from pyftpdlib import servers
from pyftpdlib.handlers import FTPHandler

os.chdir('.')
server_object = HTTPServer(server_address=('', 80), RequestHandlerClass=CGIHTTPRequestHandler)
server_object.serve_forever()

address = ("0.0.0.0", 21)
server = servers.FTPServer(address, FTPHandler)
server.serve_forever()
