from app import mongo

class Pokemon_Saved:
    collection = mongo.db.pokemonSaved


    @staticmethod
    def find_all():
        pokemonS = Pokemon_Saved.collection.find()
        return list (pokemonS)
    

    @staticmethod
    def find_by_id():
        pokemonS = Pokemon_Saved.collection.find_one({
            "id": pokemonS_id
        })
        return pokemonS
    
    @staticmethod
    def create():
        pokemonS = Pokemon_Saved.collection.insert_one(data)
        return pokemonS.inserted_id
    
    @staticmethod
    def update (pokemonS_id,data):
        pokemonS = Pokemon_Saved.collection.update_one({
            "id": pokemonS_id
        },{
            "$set": data
        })
        return pokemonS
    
    @staticmethod  
    def delete():
        return Pokemon_Saved.collection.delete_one({"_id":pokemonS_id})