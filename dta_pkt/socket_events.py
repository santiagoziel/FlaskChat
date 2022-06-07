from flask import request
from flask_socketio import emit, join_room, leave_room

from dta_pkt import socketio, db
from dta_pkt.routes import current_user
from dta_pkt.models import User

@socketio.on('connect')
def user_conecting():
    current_user.room = request.sid
    db.session.commit()
    print(f'{current_user.username} has connected with sid {request.sid}')

@socketio.on('client_disconnecting')
def disconnect_details(data):
    current_user.room = ""
    db.session.commit()
    print(f'user disconnected. {data}')

@socketio.on('new user')
def registerUser(data):
    print(f"ususario bajo nombre de {data['nombre']}")

@socketio.on('new message')
def handle_message(data):
    emit('incoming message', {'message' :data['message']})
