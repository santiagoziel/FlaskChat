from flask import request
from flask_socketio import emit, join_room, leave_room

from dta_pkt import socketio, db
from dta_pkt.routes import current_user
from dta_pkt.models import User

#when user conects to the socket it changes his room number from empty to his current room
#and lets evrybody know a new user conected
@socketio.on('connect')
def user_conecting():
    current_user.room = request.sid
    db.session.commit()
    new_user = User.query.filter(User.room == request.sid).first()
    emit('new active user', new_user.username, broadcast=True)

#when recibing message form cleint sent it to that cleint room
@socketio.on('new message')
def handle_message(data):
    # TODO: make it so its sends to current user room
    emit('incoming message', {'message' :data['message']})
#when clint disconects it removes his room from the database
@socketio.on('client_disconnecting')
def disconnect_details(data):
    current_user.room = ""
    db.session.commit()
    emit('remove active user', current_user.username, broadcast=True)
