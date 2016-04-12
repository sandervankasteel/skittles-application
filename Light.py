__author__ = 'sander'

from Database import Database
import datetime

class Light:

    def __init__(self, lightname):
        self.lightName = lightname
        # try:
        db = Database()
        cursor = db.get_cursor()
        query = ("SELECT * FROM `light_name` WHERE `name` = '%s'" % self.lightName)
        cursor.execute(query)
        row = cursor.fetchone()

        try:
            self.light_id = row[0]
            cursor.close()
            db.closeConnection()
        except TypeError:
            raise ValueError("Light doesn't exist!")


    def getStatus(self):
        db = Database()
        cursor = db.get_cursor()
        cursor.execute(("SELECT * FROM `light` WHERE `light_id` = %s ORDER BY `datetime` DESC" % self.light_id))
        row = cursor.fetchone()

        cursor.close()
        db.closeConnection()

        # item 2 of the tuple is in
        if row[2] == 1:
            return "true"
        else:
            return "false"


    def set_status(self, new_status):
        db = Database()
        cursor = db.get_cursor()
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        if new_status == "true":
            status = 1
        else:
            status = 0

        query = "INSERT INTO `light` (datetime, status, light_id) VALUES ( '{0}', '{1}', '{2}' )".format(now, status, self.light_id)
        cursor.execute(query)
        db.commit()

        db.closeConnection()
        return cursor.statement

    def create(self, name, light_type):

        return ""
