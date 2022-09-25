"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User, Personajes, Capitulos, Fav_capitulos, Fav_personajes
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/user', methods=['GET'])
def handle_hello():
    all_user=User.query.all()
    serializados=list(map(lambda user: user.serialize(),all_user))
    response_body = {
        "msg": "Hello, this is your GET /user response "
    }

    return jsonify(response_body), 200

    @app.route("/personajes", methods=['GET'])
    def get_personajes():
        return "todos los personajes"

    @app.route("/personajes/<int:personajes_id>", methods=['GET'])
    def one_personajes():
        return "solo un personaje"

    @app.route("/capitulos", methods=['GET'])
    def get_capitulos():
        return "todos los capitulos"

    @app.route("/capitulos/<int:capitulos_id>", methods=['GET'])
    def one_capitulos():
        return "solo un capitulo"


    @app.route("/user", methods=['GET'])
    def get_user():
        return "todos los usuarios"
    
    @app.route("/user/favorites", methods=['GET'])
    def one_favorites():
        return "todos favoritos"

    @app.route("/user/favorites/personajes/<int:personajes_id>", methods=['POST'])
    def get_fav_personajes():
        return "todos los personajes favoritos"

    @app.route("/user/favorites/capitulos/<int:capitulos_id>", methods=['POST'])
    def get_fav_capitulos():
        return "todos los capitulos favoritos"

    @app.route("/user/favorites/personajes/<int:personajes_id>", methods=['DELETE'])
    def get_fav_personajes():
        return "todos los personajes favoritos"

    @app.route("/user/favorites/capitulos/<int:capitulos_id>", methods=['DELETE'])
    def get_fav_capitulos():
        return "todos los capitulos favoritos"



# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
