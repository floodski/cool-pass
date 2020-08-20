#!usr/bin/python3
import sys
import os, os.path
import cherrypy
import random
import string
import sqlite3

import cherrypy
import random

class CoolPassGen(object):
    def numberGen():
        return random.choice([69,420,666])
    
    def adjectiveGen():
        return random.choice(["Shitting","Biting","Bending","Smirking","Damp","Hungry"])
    
    def nounGen():
        return random.choice(["Pope","Baby","Lover","Micky","Friend", "Cougar"])
    
    def passGen(self):
        return self.adjectiveGen() + self.nounGen() + str(self.numberGen())

    @cherrypy.expose
    @cherrypy.tools.response_headers(headers=[('Content-Type', 'text/plain')])
    def index(self):
        return CoolPassGen.passGen(CoolPassGen)
        
wsgi_app = cherrypy.Application(CoolPassGen(), '/')


    
def runMainApp():
    # Create an instance of MainApp and tell Cherrypy to send all requests under / to it. (ie all of them)
    cherrypy.tree.mount(MainApp(), "/", conf)

    cherrypy.config.update(conf)

    print ("========================================")
    print ("Helios Server")
    print ("========================================")
    print ("Initialising...")

    # Start the web server
    cherrypy.engine.start()

    # And stop doing anything else. Let the web server take over.
    cherrypy.engine.block()

if __name__ == '__main__':
    conf = {
        '/': {
            'tools.sessions.on': True,
            'tools.staticdir.root': os.path.abspath(os.getcwd())
        },
        '/static': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': './public'
        }
    }
#Run the function to start everything
    runMainApp()
	
