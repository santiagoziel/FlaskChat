from flask import request
from flask_socketio import emit, join_room, leave_room
from dta_pkt import socketio

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
