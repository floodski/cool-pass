#!usr/bin/python3
import sys
from flask import Flask, render_template
import random

app = Flask(__name__)

class CoolPassGen(object):

    dipshitMode = False

    with open("CA.txt", 'r') as reader:
        CleanAdjects = [x.rstrip() for x in reader]

    with open("CN.txt", 'r') as reader:
        CleanNouns = [x.rstrip() for x in reader]

    with open("SA.txt", 'r') as reader:
        StupidAdjects = [x.rstrip() for x in reader]

    with open("SN.txt", 'r') as reader:
        StupidNouns = [x.rstrip() for x in reader]

    
    def numberGen():
        if(CoolPassGen.dipshitMode):
            return random.choice([69,420,666,369,808])
        
        #return random.choice(["777","22"])
        return random.randint(10,999)
    
    def adjectiveGen():
        if(CoolPassGen.dipshitMode):
            #return random.choice(["Unrepentant","Remorseless","Raw","Shitting","Biting","Bending","Smirking","Damp","Hungry","Commie","Devious","Drunk"])
            return CoolPassGen.StupidAdjects[random.randint(0,(len(CoolPassGen.StupidAdjects)-1))]
        
        #return random.choice(["Lovely","Kind"])
        return CoolPassGen.CleanAdjects[random.randint(0,(len(CoolPassGen.CleanAdjects)-1))]
    
    def nounGen():
        if(CoolPassGen.dipshitMode):
            #return random.choice(["JohnLennon","Pope","Baby","Lover","Micky","Friend", "Cougar"])
            return CoolPassGen.StupidNouns[random.randint(0,(len(CoolPassGen.StupidNouns)-1))]
        
        #return random.choice(["Ducky","Puppy","Seahorse","Dandelion"])
        return CoolPassGen.CleanNouns[random.randint(0,(len(CoolPassGen.CleanNouns)-1))]
    
    def passGen():
        #print(CoolPassGen.CleanAdjects)
        return str(CoolPassGen.adjectiveGen()) + str(CoolPassGen.nounGen()) + str(CoolPassGen.numberGen())

    '''@app.route("/")
    def index():
        CoolPassGen.dipshitMode = False
        return CoolPassGen.passGen()
        #print(CoolPassGen.passGen())
        #print(CoolPassGen.CleanAdjects)'''
    @app.route('/')
    def index():
        CoolPassGen.dipshitMode = False
        passout = CoolPassGen.passGen()
        return render_template('index.html', passout=passout)
    
    @app.route("/stupid")
    def stupid():
        CoolPassGen.dipshitMode = True
        passout = CoolPassGen.passGen()
        return render_template('index.html', passout=passout)

    @app.route("/navyseal")
    def navy():
        CoolPassGen.dipshitMode = False
        return render_template('navy.html')

'''
CoolPassGen.index()
CoolPassGen.index2()'''
