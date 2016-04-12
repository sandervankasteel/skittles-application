__author__ = 'sander'

from Database import Database

class Temperature():

    def __init(self):
        self.db = Database()


    def _fetchData(self, room):
        cursor = self.db.get_cursor()
        query = ("SELECT * FROM `room` WHERE `name` = '%s'", room)



