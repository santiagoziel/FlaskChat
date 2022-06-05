from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit, join_room, leave_room
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'secret!'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'

db = SQLAlchemy(app)
socketio = SocketIO(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    room = db.Column(db.String(80), unique=True, nullable=False)
    is_in = db.relationship('Rooms', backref= 'usuario',lazy = True)
    def __repr__(self):
        return '<User %r>' % self.username
        
class Rooms(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    room_number = db.Column(db.String(80), unique=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    def __repr__(self):
        return f"{self.user_id} is in {self.room_number}"

@socketio.on('connect')
def handle_my_custom_event():
    print(f'user has connected with sid {request.sid}')

@socketio.on('client_disconnecting')
def disconnect_details(data):
    #print(f'{data['username']} user disconnected.')
    print(f'user disconnected. {data}')

@socketio.on('new message')
def handle_message(data):
    emit('incoming message', {'message' :data['message']})


@app.route('/', methods = ['GET', 'POST'])
def log_in():
    return render_template('index.html')

if __name__ == '__main__':
    socketio.run(app, debug = True)
