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
            return random.choice([69,420,666,369,808])
        
        #return random.choice(["777","22"])
        return random.randint(10,999)
    
    def adjectiveGen():
        if(CoolPassGen.dipshitMode):
            return random.choice(["Unrepentant","Remorseless","Raw","Shitting","Biting","Bending","Smirking","Damp","Hungry","Commie","Devious","Drunk"])
        
        return random.choice(["Lovely","Kind"])
    
    def nounGen():
        if(CoolPassGen.dipshitMode):
            return random.choice(["JohnLennon","Pope","Baby","Lover","Micky","Friend", "Cougar"])
        
        return random.choice(["Ducky","Puppy","Seahorse","Dandelion"])
    
    def passGen():
        return str(CoolPassGen.adjectiveGen()) + str(CoolPassGen.nounGen()) + str(CoolPassGen.numberGen())

    @app.route("/")
    def index():
        CoolPassGen.dipshitMode = False
        return CoolPassGen.passGen()
        #print(CoolPassGen.passGen())
    
    @app.route("/stupid")
    def index2():
        CoolPassGen.dipshitMode = True
        return CoolPassGen.passGen()
        #print(CoolPassGen.passGen())

'''    
CoolPassGen.index()
CoolPassGen.index2()'''
