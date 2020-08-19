import cherrypy
import random

class CoolPassGen():
    def numberGen():
        return random.choice([69,420,666])
    
    def adjectiveGen():
        return random.choice(["Shitting","Biting","Bending","Smirking","Damp","Hungry"])
    
    def nounGen():
        return random.choice(["Pope","Baby","Lover","Micky","Friend", "Cougar"])
    
    def passGen(self):
        return self.adjectiveGen() + self.nounGen() + str(self.numberGen())

    @cherrypy.expose
    def index():
        return CoolPassGen.passGen(CoolPassGen)


if __name__ == '__main__':
    cherrypy.quickstart(CoolPassGen)
