import cherrypy
import random

class CoolPassGen:
    def numberGen():
        return random.choice([69,420,666])
    
    def adjectiveGen():
        return random.choice(["Shitting","Biting","Bending","Smirking"])
    
    def nounGen():
        return random.choice(["Pope","Baby","Lover","Fiend","Friend"])
    
    def passGen():
        return CoolPassGen.adjectiveGen() + CoolPassGen.nounGen() + str(CoolPassGen.numberGen())

class main:
    print(CoolPassGen.passGen())
