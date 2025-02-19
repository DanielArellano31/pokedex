from flask import Blueprint, request
from marshmallow import ValidationError
from app.tools.response_manager import ResponseManager
from bson import ObjectId
from app.models.factory import ModelFactory

bp = Blueprint("pokemons", __name__, url_prefix="/pokemons")
RM = ResponseManager()
FP_model = ModelFactory.get_model("Pokemons")



#get all 
@bp.route("/<>", methods=["GET"])
def get_all():
    data = FP_model.find_all()
    return RM.success(data)

#get one
@bp.route("/", methods=["GET"])
def get_one(Object_id):
    pokemon = FP_model.find_by_id(Object_id)
    return RM.success(pokemon)