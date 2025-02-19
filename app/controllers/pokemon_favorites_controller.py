from flask import Blueprint, request
from app.schemas.pokemon_favorites_schema import PokemonFavoriteSchema
from marshmallow import ValidationError
from bson import ObjectId
from app.tools.response_manager import ResponseManager
from app.models.factory import ModelFactory

bp = Blueprint("pokemon_favorites", __name__, url_prefix="/pokemon_favorites")
RM = ResponseManager()
FP_model = ModelFactory.get_model("pokemon_favorites")
FP_schema = PokemonFavoriteSchema


#crea
@bp.route("/", methods =["POST"])
def create():
    try:
        data = request.json
        data = FP_schema.validate(data)
        fp = FP_model,create(data)
        return RM.success({"_id":fp})
    except ValidationError as err:
        print(err)   
        return RM.error("Es necesario enviar todos los paramentros")
    
# elimina
@bp.route("/<string:id>", methods =["DELETE"])    
def delete():
    FP_model.delete(ObjectId(id))
    return RM.success("Pokemon eliminado con exito")


#get all 
@bp.route("/<string:user_id>", methods=["GET"])
def get_all(user_id):
    data = FP_model.find_all(user_id)
    return RM.success(data)
