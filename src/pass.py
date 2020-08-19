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
        return adjectiveGen() + nounGen() + numberGen()

class main:
    pre = "key"
    post = "john"
    
    print(CoolPassGen.numberGen())
    
    print(pre + post)
