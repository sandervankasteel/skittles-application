__author__ = 'sander'

import mysql.connector
import configparser

class Database():

    def __init__(self):
        configFile = configparser.ConfigParser()
        configFile.read('config.ini')

        self.cnx = mysql.connector.connect(user = configFile['Database']['User'],
                                             password = configFile['Database']['Password'],
                                             host = configFile['Database']['Host'],
                                             database = configFile['Database']['Database']
                                             )
    def get_connection(self):
        return self.cnx

    def get_cursor(self):
        return self.cnx.cursor(buffered=True)

    def commit(self):
        self.cnx.commit()

    def get_connector(self):
        return self.cnx.connector

    def closeConnection(self):
        self.cnx.close()