"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)

# create the jackson family object
jackson_family = FamilyStructure("Jackson")

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/members', methods=['GET'])
def handle_hello():

    # this is how you can use the Family datastructure by calling its methods
    members = jackson_family.get_all_members()
    response_body = {
        "family": members
    }


    return jsonify(response_body), 200

@app.route("/addmembers",methods=["POST"])
def new():
    body=request.get_json()
    members=jackson_family.add_member(body)
    res={
        "family": members,
        "mensaje":"se creo un usuario"
    }
    return jsonify(res),200

@app.route("/eliminar/<int:id>",methods=["DELETE"])
def borrar(id):
    members=jackson_family.delete_member(id)
    if members is False:
        statuscode =400
        res={
            "family": members,
            "mensaje":"no se encontro un usuario"
        }
    else:
        statuscode =200
        res={
            "family": members,
            "mensaje":"se elimino un usuario"
        }
        
    return jsonify(res),statuscode

@app.route("/obtenerporid/<int:id>",methods=["GET"])
def obtener(id):
    members=jackson_family.get_member(id)
    if members is None :
        statuscode=400
        res={
        "family": members,
        "mensaje":"no se obtiene un usuario"
    }
    else:
        statuscode=200
        res={
            "family": members,
            "mensaje":"se obtiene un usuario"
        }

    return jsonify(res),statuscode


# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)
