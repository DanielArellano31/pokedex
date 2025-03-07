from app import mongo
from app.models.super_class import SuperClass

class Pokemon(SuperClass): 
    def init(self):
        super().init("pokemons")

    def create(self, data):
        raise NotImplementedError("Los pokemones no se pueden crear")
    
    def delete(self, object_id):
        raise NotImplementedError("Los pokemones no se pueden eliminar")
    
    def update(self, object_id,data):
        raise NotImplementedError("Los pokemones no se pueden actualizar")