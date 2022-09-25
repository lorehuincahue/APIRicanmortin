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
    return jsonify(serializados), 200

    @app.route("/personajes", methods=['GET'])
    def get_personajes():
        all_personajes=Personajes.query.all()
        print(all_personajes)
        return "todos los personajes"
        all_personajes=list(map(lambda personajes:personajes.serialize(), all_personajes))
        return jsonify(all_personajes)

    @app.route("/personajes/<int:personajes_id>", methods=['GET'])
    def one_personajes(personajes_id):
        one=Personajes.query.get(personajes_id)
        return jsonify(one.serialize())

    @app.route("/capitulos", methods=['GET'])
    def get_capitulos():
        all_capitulos=Capitulos.query.all()
        print(all_capitulos)
        return "todos los capitulos"
        all_capitulos=list(map(lambda capitulos:capitulos.serialize(), all_capitulos))
        return jsonify(all_capitulos)

    @app.route("/capitulos/<int:capitulos_id>", methods=['GET'])
    def one_capitulos(capitulos_id):
        uno=Capitulos.query.get(capitulos_id)
        return jsonify(uno.serialize())


      
    @app.route("/user/favorites", methods=['GET'])
    def one_favorites():
        return "todos favoritos"

    @app.route("/favorites/personajes/<int:personajes_id>", methods=['POST'])
    def add_personajes_fav(personajes_id):
        one = Personajes.query.get(personajes_id) #busqueda solo por el pk
        user = User.query.get(1)
        if(one):
            new_fav = Fav_personajes()
            new_fav.email = user.email
            new_fav.personajes_id = personajes_id
            db.session.add(new_fav)
            db.session.commit()
            return "Hecho!"
        else:
            raise APIException("no existe el personaje", status_code=404)

    @app.route("/favorites/capitulos/<int:capitulos_id>", methods=['POST'])
    def add_capituloss_fav(capitulos_id):
            uno = Capitulos.query.get(capitulos_id) #busqueda solo por el pk
            user = User.query.get(1)
            if(uno):
                new_fav = Fav_capitulos()
                new_fav.email = user.email
                new_fav.capitulos_id = capitulos_id
                db.session.add(new_fav)
                db.session.commit()
                return "Hecho!"
            else:
                raise APIException("no existe el capitulo", status_code=404)


    @app.route("/favorites/personajes/<int:personajes_id>", methods=['DELETE'])
    def delete_personajes_fav(personajes_id):
        one = Fav_personajes.query.filter_by(personajes_id=personajes_id).first()
        if(one):
            db.session.delete(one)
            db.session.commit()
            return "eliminado"
        else:
            raise APIException("no existe el personaje", status_code=404)

    @app.route("/favorites/capitulos/<int:capitulos_id>", methods=['DELETE'])
    def delete_capitulos_fav(capitulos_id):
            uno = Fav_capitulos.query.filter_by(capitulos_id=capitulos_id).first()
            if(uno):
                db.session.delete(uno)
                db.session.commit()
                return "eliminado"
            else:
                raise APIException("no existe el personaje", status_code=404)


# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
