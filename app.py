import sys
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
        
wsgi_app = cherrypy.Application(CoolPassGen(), '/')

if __name__ == '__main__':
	from wsgiref.simple_server import make_server

    #cherrypy.config.update( {'server.socket_host': '0.0.0.0'} )
        
	httpd = make_server('', 6600, wsgi_app)
	httpd.serve_forever()
	
