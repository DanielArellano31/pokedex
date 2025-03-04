from app import mongo
from app.models.super_class import SuperClass
from bson import ObjectId


class PokemonFavorites(SuperClass):
    def init(self):
        super().init("pokemon_favorites")

 
 
    def update(self, ObjectId,data):
        raise NotImplementedError("Los pokemones no se pueden actualizar")
    
    def find_by_id(self,object_id):
        datum = self.collection.find_one({
            "_id": object_id
        })
        return datum
    def find_all(self,user_id):
        data = self.collection.find({"user_id": ObjectId(user_id)})
        for datum in data:
            datum["user_id"]=str(datum["user_id"])
            datum["pokemon_id"]=str(datum["pokemon_id"])
            datum["_id"]=str(datum["_id"])
        return data
    
    