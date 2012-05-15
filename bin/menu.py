import os

from google.appengine.ext import db
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

# Main Page
class MainPage(webapp.RequestHandler):
    def get(self):
        # menu write out the JSON
        self.response.out.write("""            
                [
                    {
                        "text": "Home",
                        "url": "/"
                    },                    
                    {
                        "text": "Adopt",
                        "url": "/Adopt",
                        "sub_items" :
                        [
                            {
                                "text" : "Available Pets",
                                "url" : "/"
                            },
                            {
                                "text" : "Adoption Process",
                                "url" : "/"
                            },
                            {
                                "text" : "Featured Animals",
                                "url" : "/"
                            }
                        ]       
                    },
                    {
                        "text": "Support Us",
                        "url": "/SupportUs",
                        "sub_items" :
                        [
                            {
                                "text" : "Make a Donation",
                                "url" : "/"
                            },
                            {
                                "text" : "Planned Giving",
                                "url" : "/"
                            },
                            {
                                "text" : "Sponsor a Cage",
                                "url" : "/"
                            },
                            {
                                "text" : "Become a Member",
                                "url" : "/"
                            },
                            {
                                "text" : "Event Donation",
                                "url" : "/"
                            },
                            {
                                "text" : "Corporate Sponsors",
                                "url" : "/"
                            },
                            {
                                "text" : "Other Ways to Help",
                                "url" : "/"
                            },
                            {
                                "text" : "Our Wish List",
                                "url" : "/"
                            }
                        ]       
                    },
                    {
                        "text": "Volunteer",
                        "url": "/Volunteer",
                        "sub_items" :
                        [
                            {
                                "text" : "Volunteer Program",
                                "url" : "/"
                            },
                            {
                                "text" : "Volunteer Positions",
                                "url" : "/"
                            },
                            {
                                "text" : "Foster Program",
                                "url" : "/"
                            }
                        ]       
                    },
                    {
                        "text": "Events",
                        "url": "/Events",
                        "sub_items" :
                        [
                            {
                                "text" : "Calendar of Events",
                                "url" : "/"
                            },
                            {
                                "text" : "Rescue Rock-Off",
                                "url" : "/"
                            },
                            {
                                "text" : "Woof, Wag & Wine",
                                "url" : "/"
                            },
                            {
                                "text" : "Mutt Strut",
                                "url" : "/"
                            },
                            {
                                "text" : "Black Cat Ball",
                                "url" : "/"
                            }
                        ]   
                    },
                    {
                        "text": "Programs",
                        "url": "/Programs",
                        "sub_items" :
                        [
                            {
                                "text" : "Angel Fund",
                                "url" : "/"
                            },
                            {
                                "text" : "Enrichment Program",
                                "url" : "/"
                            },
                            {
                                "text" : "Humane Education",
                                "url" : "/"
                            },
                            {
                                "text" : "Canine Happy Hour",
                                "url" : "/"
                            },
                            {
                                "text" : "Bully Breed Program",
                                "url" : "/"
                            },
                            {
                                "text" : "Recycling Program",
                                "url" : "/"
                            },
                            {
                                "text" : "Educational Tours for Children",
                                "url" : "/"
                            },
                            {
                                "text" : "PetFix",
                                "url" : "/"
                            }
                        ]
                    },
                    {
                        "text": "Services",
                        "url": "/Services",
                        "sub_items" :
                        [
                            {
                                "text" : "24 Hour Animal Rescue",
                                "url" : "/"
                            },
                            {
                                "text" : "Humane Investigations",
                                "url" : "/"
                            },
                            {
                                "text" : "Pet Therapy",
                                "url" : "/"
                            },
                            {
                                "text" : "Microchip Clinic",
                                "url" : "/"
                            }
                        ]   
                    },
                    {
                        "text": "About Us",
                        "url": "/About",
                        "sub_items" :
                        [
                            {
                                "text" : "Annual Report",
                                "url" : "/"
                            },
                            {
                                "text" : "In the Media",
                                "url" : "/"
                            },
                            {
                                "text" : "Careers / Internships",
                                "url" : "/"
                            },
                            {
                                "text" : "Hours",
                                "url" : "/"
                            },
                            {
                                "text" : "Our Staff",
                                "url" : "/"
                            },
                            {
                                "text" : "The Board of Directors",
                                "url" : "/"
                            }
                        ]   
                    },
                    {
                        "text": "Pet Tips",
                        "url": "/PetTips",
                        "sub_items" :
                        [
                            {
                                "text" : "Articles",
                                "url" : "/"
                            }
                        ]   
                    },
                    {
                        "text": "Contact",
                        "url": "/Contact",
                        "sub_items" :
                        [
                            {
                                "text" : "General Contact Info",
                                "url" : "/"
                            },
                            {
                                "text" : "Facebook",
                                "url" : "/"
                            },
                            {
                                "text" : "Twitter",
                                "url" : "/"
                            }
                        ]   
                    }                                        
                ]
            """)
#{
#    "text": "New Animal",
#    "url": "/Create"
#},
#{
#    "text": "Located Animals",
#    "url": "/LocatedAnimals" ,  
#    "sub_items" :
#    [
#        {
#            "text" : "Dogs",
#            "url" : "/"
#        },
#        {
#            "text" : "Cats",
#            "url" : "/"
#        }
#    ]                     
#}

# Run our application
application = webapp.WSGIApplication(
                                     [('/Menu', MainPage)
                                      ],debug=True)        

def main():
    run_wsgi_app(application)
    
if __name__ == "__main__":
    main()