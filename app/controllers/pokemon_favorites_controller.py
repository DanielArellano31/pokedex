from flask import Blueprint, request
from app.schemas.pokemon_favorites_schema import PokemonFavoriteSchema
from marshmallow import ValidationError
from bson import ObjectId
from app.tools.response_manager import ResponseManager
from app.models.factory import ModelFactory
from flask_jwt_extended import jwt_required,get_jwt_identity


bp = Blueprint("pokemon_favorites", __name__, url_prefix="/pokemon_favorites")
RM = ResponseManager()
FP_model = ModelFactory.get_model("pokemon_favorites")
FP_schema = PokemonFavoriteSchema


#crea
@bp.route("/", methods =["POST"])
@jwt_required()
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
@jwt_required()
def delete():
    FP_model.delete(ObjectId(id))
    return RM.success("Pokemon eliminado con exito")


#get all 
@bp.route("/", methods=["GET"])
@jwt_required()
def get_all(user_id):
    user_id = get_jwt_identity()
    data = FP_model.find_all(user_id)
    return RM.success(data)
