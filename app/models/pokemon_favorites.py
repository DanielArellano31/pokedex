from app import mongo
from app.models.super_class import SuperClass

class PokemonFavorites(SuperClass):
    def init(self):
        super().init("pokemon_favorites")
