from models.user import db

class Guest(db.Model):
    __tablename__ = 'guests'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    occupation = db.Column(db.String(120), nullable=False)
    appearances = db.relationship('Appearance', backref='guest', cascade='all, delete-orphan')

    def __repr__(self):
        return f"<Guest(name={self.name}, occupation={self.occupation})>"

    # Additional methods for interacting with guest data can be added here.