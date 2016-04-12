__author__ = 'sander'
import cherrypy
import os
from Webpages import Webpages

class WebServer():

    def __init__(self, addr, port):
        cherrypy.server.socket_port = int(port)
        cherrypy.server.socket_host = addr

    def start_server(self):
        cherrypy.quickstart(Webpages(), '/',
            {
                '/' : {
                    'tools.sessions.on': True,
                    'tools.staticdir.root': os.path.abspath(os.getcwd() + '/html')
                },
                '/js': {
                    'tools.staticdir.on' : True,
                    'tools.staticdir.dir' : './js'
                },
                '/css': {
                    'tools.staticdir.on' : True,
                    'tools.staticdir.dir' : './css'
                }
            }
        )

    def close_server(self):
        cherrypy.engine.exit()

    def restart_server(self):
        cherrypy.engine.restart()