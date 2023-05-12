from flask import Flask, render_template
from flask_socketio import SocketIO, send, emit
import os
from gevent import monkey
monkey.patch_all()

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app,
                    logger=True,
                    engineio_logger=True,
                    cors_allowed_origins="*",
                    message_queue='redis://:eYVX7EwVmmxKPCDmwMtyKVge8oLd2t81@redis:6379/0')



@socketio.on('message')
def handle_message(data):
    print('received message: ' + data)

@socketio.on('json')
def handle_json(json):
    print('received json: ' + str(json))

@socketio.on('connect')
def test_connect(auth):
    emit('my response', {'data': 'Connected', "host":os.uname()[1]})

@socketio.on('disconnect')
def test_disconnect():
    print('Client disconnected')

if __name__ == '__main__':
    socketio.run(app)