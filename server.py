import random
import string
import cherrypy
import os 
from pathlib import Path 
config = {
'/static': {
'tools.staticdir.on' : True,
"tools.staticdir.dir": os.getcwd() + "\\static" }
}
cherrypy.config.update(config)
print (cherrypy.config) 

class StringMaker(object):
   @cherrypy.expose
   def index(self):
      return "Hello! How are you?"
   
   @cherrypy.expose
   def generate(self, length=9):
      return ''.join(random.sample(string.hexdigits, int(length)))

   @cherrypy.expose
   def greeting(self, name):
       return "Hello " + name + "!"
		
if __name__ == '__main__':
   cherrypy.quickstart(StringMaker (), '/', config)
