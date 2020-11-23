#!usr/bin/python3
import sys
from flask import Flask
import random
import sqlite3

import cherrypy
import random

app = Flask(__name__)

class CoolPassGen(object):
    
    dipshitMode = False
    
    def numberGen():
        if(CoolPassGen.dipshitMode):
            return random.choice([69,420,666])
        
        return random.choice(["777","22"])
    
    def adjectiveGen():
        if(CoolPassGen.dipshitMode):
            return random.choice(["Shitting","Biting","Bending","Smirking","Damp","Hungry"])
        
        return random.choice(["Lovely","Kind"])
    
    def nounGen():
        if(CoolPassGen.dipshitMode):
            return random.choice(["Pope","Baby","Lover","Micky","Friend", "Cougar"])
        
        return random.choice(["Ducky","Puppy"])
    
    def passGen():
        return str(CoolPassGen.adjectiveGen()) + str(CoolPassGen.nounGen()) + str(CoolPassGen.numberGen())

    @app.route("/")
    def index(string):
        dipshitMode = False
        return CoolPassGen.passGen()
        #print(CoolPassGen.passGen())
    
    @app.route("/stupid")
    def index2(string):
        dipshitMode = True
        return CoolPassGen.passGen()
        #print(CoolPassGen.passGen())

'''    
CoolPassGen.index("ok")
CoolPassGen.index2("dumb")'''
