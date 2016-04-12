__author__ = 'sander'

import io
import time

class Logging():

    def __init__(self, logfile):
        self.file = io.open(logfile, 'a')

    def append(self, message):
        date = time.strftime("%c")
        self.file.write("[" + date + "] " + message + "\n")

    def appendRequest(self, message):
        self.file.write(message)

    def close(self):
        self.file.close()
