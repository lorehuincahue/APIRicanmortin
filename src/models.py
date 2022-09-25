from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.email

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
        }

class Personajes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    personajes = db.Column(db.String(30), unique=True, nullable=False)
    
    def __repr__(self):
        return '<Personajes %r>' % self.personajes

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "status": self.status,
            "species": self.species,
            "gender": self.gender,
            
        }

class Capitulos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    capitulos = db.Column(db.String(30), unique=False, nullable=False)
    
    def __repr__(self):
        return '<Capitulos %r>' % self.capitulos

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "air_date": self.air_date,
            "episode": self.episode,
    
        }

class Fav_personajes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    personajes_id = db.Column(db.Integer, db.ForeignKey('personajes.id') )
    email =  db.Column(db.String(120), db.ForeignKey('user.email'))
    rel_user = db.relationship('User')
    rel_pj = db.relationship('Personajes')

    def __repr__(self):
        return '<Fav_personajes %r>' % self.email

    def serialize(self):
        return {
            "id": self.id,
            "personajes_id": self.personajes_id,
            "email": self.email
        }

class Fav_capitulos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    capitulos_id = db.Column(db.Integer, db.ForeignKey('capitulos.id') )
    email =  db.Column(db.String(120), db.ForeignKey('user.email'))
    rel_user = db.relationship('User')
    rel_cap = db.relationship('Capitulos')

    def __repr__(self):
        return '<Fav_capitulos %r>' % self.email

    def serialize(self):
        return {
            "id": self.id,
            "capitulos_id": self.capitulos_id,
            "email": self.email
        }