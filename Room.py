__author__ = 'sander'

from Database import Database

class Room():
    def __init__(self, roomnaam):
        self.room_name = roomnaam

        db = Database()
        cursor = db.get_cursor()
        cursor.execute(("SELECT * FROM `rooms` WHERE `name` = '%s'" % self.room_name))
        row = cursor.fetchone()

        try:
            self.room_id = row[0]

        except TypeError:
            raise ValueError("Room doesn't exist!")

