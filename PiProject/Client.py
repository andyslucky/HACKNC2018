
# This is code to be run on the Raspberry PI
import socket
import serial

HOST = '172.20.10.2'  # The server's hostname or IP address
PORT = 2521        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    print("connecting...")
    s.connect((HOST, PORT))
    print("done.")
    s.sendall(b'Hello, world')
    print("awaiting your msg")
    data = s.recv(1024)
    print(data)

print('Received', repr(data))

def set_light(state):
  sendByte = ['o', 'O'][state]


def get_light(state):
  pass
