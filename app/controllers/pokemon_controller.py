from flask import Blueprint
from app.tools.response_manager import ResponseManager
from bson import ObjectId
from app.models.factory import ModelFactory
from flask_jwt_extended import jwt_required 


bp = Blueprint("pokemons", __name__, url_prefix="/pokemon")
RM = ResponseManager()
FP_model = ModelFactory.get_model("pokemons")



#get all 
@bp.route("/", methods=["GET"])
@jwt_required()
def get_all():
    data = FP_model.find_all()
    return RM.success(data)

#get one
@bp.route("/", methods=["GET"])
@jwt_required()
def get_pokemon(Pokemon_id):
    pokemon = FP_model.find_by_id(ObjectId(Pokemon_id))
    return RM.success(pokemon)