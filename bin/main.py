import os

from google.appengine.api import users
from google.appengine.ext import db
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from google.appengine.ext.webapp.util import run_wsgi_app

# import our Models
from lib.models import lost_animal
             
# Request Handler for getting the image from the datastore
class AnimalImage(webapp.RequestHandler):
    def get(self):
        animal = getAnimalByName(self.request.get('img_id'))
        if (animal and animal.image):
            #if animal.image:
            self.response.headers['Content-Type'] = "image/png"
            self.response.out.write(animal.image)        

# Gets an Animal Image from the datastore
def getAnimalByName(img_id):
    animal = lost_animal.get(img_id)
    if ( animal and animal.image ):
        return animal
    else:
        return None                       

# Add an animal to the collection 
class NewAnimal(webapp.RequestHandler):
    def get(self):
        user = users.get_current_user()        
        if user:
            url = users.create_logout_url("/")
            greeting = ("Welcome, %s " % (user.nickname()))
        else:
            url = users.create_login_url("/")
            greeting = "Sign in or Register!"
        # get all the Lost Animals and display them in a table row
        animals = lost_animal.all().fetch(10)
        
        template_values = { 
                           "animals" : animals,
                           "user" : user,
                           "login_url" : url,
                           "greeting" : greeting
                           }
        
        path = os.path.join(os.path.dirname(__file__), '../templates/create.html')
        self.response.out.write(template.render(path, template_values))
        
class ListAnimals(webapp.RequestHandler):
    def get(self):
        user = users.get_current_user()        
        if user:
            url = users.create_logout_url("/")
            greeting = ("Welcome, %s" % (user.nickname()))
        else:
            url = users.create_login_url("/")
            greeting = "Sign in or Register!"
        # get all the Lost Animals and display them in a table row
        #
        # TODO:  Implement Paging here
        #
        animals = lost_animal.all().fetch(10)
        
        template_values = { 
                           "animals" : animals,
                           "user" : user,
                           "login_url" : url,
                           "greeting" : greeting
                           }
        
        path = os.path.join(os.path.dirname(__file__), '../templates/index.html')
        self.response.out.write(template.render(path, template_values))       
                        
# Save image handler
class SaveLostAnimal(webapp.RequestHandler):
    def post(self):        
        # save the animal that was entered in the form
        lostAnimal = lost_animal()
        lostAnimal.name = self.request.get("name")
        lostAnimal.image = db.Blob(self.request.get("image"))

        # save the new image
        lostAnimal.put()
        
        # return to home page
        self.redirect('/')
 
class Map(webapp.RequestHandler):
    def get(self):
        user = users.get_current_user()        
        if user:
            url = users.create_logout_url("/")
            greeting = ("Welcome, %s" % (user.nickname()))
        else:
            url = users.create_login_url("/")
            greeting = "Sign in or Register!"
    
        template_values = { 
                           "user" : user,
                           "login_url" : url,
                           "greeting" : greeting
                           }
        
        path = os.path.join(os.path.dirname(__file__), '../templates/map.html')
        self.response.out.write(template.render(path, template_values))

# *******************************
#
# Handlers 
#        
# *******************************
class Home(webapp.RequestHandler):
    def get(self):
        user = users.get_current_user()        
        if user:
            url = users.create_logout_url("/")
            greeting = ("Welcome, %s" % (user.nickname()))
            url_text = "[sign out]"
        else:
            url = users.create_login_url("/")
            greeting = ""
            url_text = "Sign in!"
                    
        # get all the Lost Animals and display them in a table row
        animals = lost_animal.all().fetch(10)
        
        template_values = { 
                           "animals" : animals,
                           "user" : user,
                           "login_url" : url,
                           "greeting" : greeting,
                           "url_text" : url_text
                           }
        
        path = os.path.join(os.path.dirname(__file__), '../templates/index.html')
        self.response.out.write(template.render(path, template_values))        
                                                                                            
# Run our application
application = webapp.WSGIApplication(
                                     [('/', Home),
                                      ],debug=True)        

def main():
    run_wsgi_app(application)
    
if __name__ == "__main__":
    main()