from google.appengine.ext import db

# Our LostAnimal storage object
class lost_animal(db.Model):
    name = db.StringProperty(multiline=False)    
    image = db.BlobProperty(default=None)
    removeAfter = db.DateProperty(auto_now_add=True)
    createDate = db.DateTimeProperty(auto_now_add=True)
    
class menu_item(db.Model):
    text = db.StringProperty(multiline=False)
    description = db.StringProperty(multiline=False)
    url = db.StringProperty(multiline=False)
        
