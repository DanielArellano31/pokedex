from app import mongo
from app.models.super_class import SuperClass

class User(SuperClass):
 def init(self):
     super().init("users")

def find_all(self):
   raise NotImplementedError("No es necesario obtener todos los usuarios")

