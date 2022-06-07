from dta_pkt import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    room = db.Column(db.String(80), unique=True)
    is_in = db.relationship('Rooms', backref= 'usuario',lazy = True)
    def __repr__(self):
        return '<User %r>' % self.username

class Rooms(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    room_number = db.Column(db.String(80), unique=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    def __repr__(self):
        return f"{self.user_id} is in {self.room_number}"
