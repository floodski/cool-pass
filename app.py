#!usr/bin/python3
import sys
from flask import Flask
import random
import sqlite3

import cherrypy
import random

app = Flask(__name__)

class CoolPassGen(object):
    def numberGen():
        return random.choice([69,420,666])
    
    def adjectiveGen():
        return random.choice(["Shitting","Biting","Bending","Smirking","Damp","Hungry"])
    
    def nounGen():
        return random.choice(["Pope","Baby","Lover","Micky","Friend", "Cougar"])
    
    def passGen():
        return CoolPassGen.adjectiveGen() + CoolPassGen.nounGen() + str(CoolPassGen.numberGen())

    @app.route("/")
    def index():
        return CoolPassGen.passGen()
    
    @app.route("/stupid")
    def index():
        return CoolPassGen.passGen()
