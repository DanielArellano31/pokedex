from app.models.pokemon import Pokemon
from app.models.pokemon_favorites import Pokemon_Saved
from app.models.users import Users


class ModelFactory:
    @staticmethod
    def get_model(collection_name):
        models = {
            "users": Users,
            "pokemons":Pokemon,
            "pokemon_favorites": Pokemon_Saved
        }
        if collection_name in models:
            return models[collection_name]()
        raise ValueError(f"La coleccion enviada :{collection_name} no existe")