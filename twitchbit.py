import pathlib
import socket

SERVER = 'irc.chat.twitch.tv'
PORT = 6667
NICKNAME = pathlib.Path('./nick.txt').read_text()
TOKEN = pathlib.Path('./token.txt').read_text()
CHANNEL = pathlib.Path('./channel.txt').read_text()
CONTROLS = {
    'w': 'hard drop', 
    's': 'soft drop', 
    'a': 'move left', 
    'd': 'move right', 
    'j': 'rotate left', 
    'l': 'rotate right',
    'i': 'rotate 180',
    'b': 'hold',
}

sock = socket.socket()
sock.connect((SERVER, PORT))

sock.send(f'PASS {TOKEN}\n'.encode('utf-8'))
sock.send(f'NICK {NICKNAME}\n'.encode('utf-8'))
sock.send(f'JOIN {CHANNEL}\n'.encode('utf-8'))

while True:
    resp = sock.recv(2048).decode('utf-8')
    if resp.startswith('PING'):
        sock.send('PONG\n'.encode('utf-8'))
    elif len(resp) > 0:
        for x in resp.splitlines():
            message = x[x.find(CHANNEL) + len(CHANNEL) + 2:]
            for y in CONTROLS:
                if message.lower() == y:
                    print(CONTROLS[y])