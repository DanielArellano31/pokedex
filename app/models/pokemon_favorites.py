from app import mongo
from app.models.super_class import SuperClass
from bson import ObjectId
class PokemonFavorites(SuperClass):
    def init(self):
        super().init("pokemon_favorites")

 
 
    def update(self, object_id,data):
        raise NotImplementedError("Los pokemones no se pueden actualizar")
    
    def find_by_id(self,object_id):
        datum = self.collection.find_one({
            "_id": object_id
        })
        return datum
    def find_all(self,user_id):
        data = self.collection.find({"user_id": ObjectId(user_id)})
        return data
    