import cherrypy
import random

class CoolPassGen:
    def numberGen():
        return random.choice([69,420,666])
    
    def adjectiveGen():
        return "Shitting"
    
    def nounGen():
        return "Pope"
    
    def passGen():
        return CoolPassGen.adjectiveGen() + CoolPassGen.nounGen() + str(CoolPassGen.numberGen())

class main:
    print(CoolPassGen.passGen())
