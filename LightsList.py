
__author__ = 'sander'
 
import Database
from Light import Light
 
class LightsList():

    def __init__(self):
        self.all_lights = []
 
        db = Database.Database()
        cursor = db.get_cursor()
        cursor.execute("SELECT * FROM `light_name`")
 
        for name in cursor:
            self.all_lights.append(Light(name[1]))
 
        cursor.close()
        db.closeConnection()

    def get_lights(self):
        return self.all_lights