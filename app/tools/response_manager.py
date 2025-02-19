from flask import jsonify

#sustituir jsonify para hacerlo dinamico y que no se repita en todos los controladores
class ResponseManager:
   #validar si data es un string para usar el axios error
    def success(self, data):
        if type (data) == "str":
            data ={
                "message":data
            }
        return jsonify(data),200
    
    def error(self,data="invalid request"):
         if type (data) == "str":
            data ={
                "message":data
            }
            return jsonify(data), 400
    def error_server(self,data="SERVER ERROR"):
         if type (data) == "str":
            data ={
                "message":data
            }
            return jsonify(data), 500