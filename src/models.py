from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return f"user {self.email} and id {self.id}"

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "is_active": self.is_active
            # do not serialize the password, it's a security breach
        }

class Characters(db.Model):
    __tablename__ = "characters"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    height = db.Column(db.String(50), nullable=False)
    planet_id = db.Column(db.Integer, db.ForeignKey("planet.id"), nullable=False)
    planet_relationship = db.relationship("Planet")

    def __repr__(self):
        return f"Character {self.name} with ID {self.id}"

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "height": self.height,
            "planet_id": self.planet_id
        }

class Planet(db.Model):
    __tablename__ = "planet"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    climate = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f"Planet {self.name} with climate {self.climate}"

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "climate": self.climate
        }

class Favorite(db.Model):
    __tablename__ = "favorite"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    planet_id = db.Column(db.Integer, db.ForeignKey("planet.id"), nullable=True)
    character_id = db.Column(db.Integer, db.ForeignKey("characters.id"), nullable=False)
    user = db.relationship(User)
    planet_relationship = db.relationship(Planet)
    character_relationship = db.relationship(Characters)

    def __repr__(self):
        return f"Favorite for user {self.user_id}, character {self.character_id}, planet {self.planet_id}"

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "planet": self.planet_relationship[0].serialize() if self.planet_relationship else None,
            "character": self.character_relationship[0].serialize()
        }