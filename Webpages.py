__author__ = 'sander'

import cherrypy
import os
from LightsList import LightsList
from Light import Light

from jinja2 import Environment, FileSystemLoader

env = Environment(loader = FileSystemLoader(os.getcwd() + '/html/templates'))

class LightControl(object):

    @cherrypy.expose
    def index(self):
        template = env.get_template('lights/index.html')
        lights = LightsList()
        return template.render(lights = lights.get_lights())

    @cherrypy.expose
    def add(self):
        template = env.get_template('lights/add.html')
        return template.render()

    @cherrypy.expose
    def update(self, lightName, status):
        light = Light(lightName)
        light.set_status(status)
        return "Het gaat om lamp " + lightName + " en zijn nieuwe status is " + status

    @cherrypy.expose
    def stats(self):
        return "Statistieken van alle lampen"

class Stats(object):

    @cherrypy.expose
    def index(self):
        return "stats page"

class Temperature(object):

    @cherrypy.expose
    def index(self):
        template = env.get_template('temperature.html')
        return template.render()

class Api(object):

    @cherrypy.expose
    @cherrypy.tools.json_out()

    def index(self):
        return {'miauw': 'said skittles' }

class Lights(object):
    @cherrypy.expose
    @cherrypy.tools.json_out()
    def index(self):
        allLights = LightsList()
        # some comment
        lights = []
        for light in allLights.get_lights():
            lights.append({'status': light.getStatus(), 'name' : light.lightName})
        return lights

class LightApi(object):
    @cherrypy.expose
    def index(self):
        return "false"

class LightUpdate(object):
    @cherrypy.expose()
    @cherrypy.tools.allow(methods=['POST'])
    def index(self, lightname, status):
        light = Light(lightname)
        light.set_status(status)

class ApiTemperature(object):
    @cherrypy.expose
    @cherrypy.tools.allow(methods=['POST'])
    @cherrypy.tools.json_out()
    def index(self, room):
        return {'room' : room, 'temperature' : 20.5}

class Webpages():
    lights = LightControl()
    stats = Stats()
    temperature = Temperature()
    api = Api()

    api.lights = Lights()
    api.light = LightApi()
    api.light.update = LightUpdate()
    api.temperature = ApiTemperature()

    @cherrypy.expose
    def index(self):
        template = env.get_template('index.html')
        return template.render()

