__author__ = 'sander'

import socketserver
import configparser
import socket
import threading
from Light import Light
from Logging import Logging
from Webserver import WebServer

class EchoRequestHandler(socketserver.BaseRequestHandler):

    def handle(self):
        data = self.request.recv(1024).decode("UTF-8").strip('\r\n') # Get the data from the client and immediatly strip off \r\n chars and make a String out of it!

        if(len(data) > 1):
            try:
                lightName = Light(data.rsplit('get light ')[1])
                self.request.send(bytes(lightName.getStatus().encode("UTF-8")))

                logging.append("request for " + data + " from client " + self.client_address[0])
            except ValueError:
                logging.append("ERROR! light " + data.rsplit('get light ')[1] + " doesn't exist!")
                self.request.send(b"false")
        else :
            self.request.send(b"false")

if __name__ == '__main__':

    # First let's import some config files!
    configFile = configparser.ConfigParser()
    configFile.read('config.ini')

    logging = Logging(configFile['General']['LogFile'])

    address = (configFile['Server']['IP'], int(configFile['Server']['Port']))
    server = socketserver.TCPServer(address, EchoRequestHandler)
    ip, port = server.server_address # find out what port we were given

    t = threading.Thread(target=server.serve_forever)
    t.setDaemon(True) # don't hang on exit
    t.start()

    # Start the webserver
    wserver = WebServer(configFile['Web']['IP'], configFile['Web']['Port'])
    wserver.start_server()

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        server.shutdown()
        wserver.close_server()
        logging.close() # Close the logging file


