import os

from google.appengine.api import users
from google.appengine.ext import db
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from google.appengine.ext.webapp.util import run_wsgi_app

# import our Models
from lib.models import lost_animal

# Main Page
class MainPage(webapp.RequestHandler):
    def get(self):
        user = users.get_current_user()        
        if user:
            url = users.create_logout_url("/")
            greeting = ("Welcome, %s" % (user.nickname()))
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
        
        path = os.path.join(os.path.dirname(__file__), '../templates/located.html')
        self.response.out.write(template.render(path, template_values))

# Run our application
application = webapp.WSGIApplication(
                                     [('/LocatedAnimals', MainPage),
                                      ],debug=True)        

def main():
    run_wsgi_app(application)
    
if __name__ == "__main__":
    main()