import os
import logging

from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from google.appengine.ext.webapp.util import run_wsgi_app



providers = {
    'Google'    : 'www.google.com/accounts/o8/id',
    'Yahoo'     : 'yahoo.com',
    'AOL'       : 'aol.com',
    'MyOpenID'  : 'myopenid.com'
}

# Dictionary for our login urls
logins = {}

# Login Handler        
class OpenIDLogin(webapp.RequestHandler):
    def get(self):
        user = users.get_current_user()        
        if not user:
            for name, uri in providers.items():
                logins[name] = users.create_login_url(federated_identity=uri)

        template_values = { 
                           "user" : user,
                           "logins" : logins                           
                           }
        
        path = os.path.join(os.path.dirname(__file__), '../templates/login.html')
        self.response.out.write(template.render(path, template_values))                
        
# Run our application
application = webapp.WSGIApplication(
                                     [('/_ah/login_required', OpenIDLogin)                                      
                                      ],debug=True)        

def main():
    run_wsgi_app(application)
    
if __name__ == "__main__":
    main()        

