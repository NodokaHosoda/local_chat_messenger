import sys
import socket
import os

name = input('type your name : ')
byte_name = name.encode('utf-8')

sock = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)

server_address = os.path.expanduser('~/udp_socket_file')

address = os.path.expanduser('~/udp_client_socket_file')

if(os.path.exists(address)):
    os.remove(address)

sock.bind(address)

try:
    print('sending {!r}'.format(name))
    sent = sock.sendto(byte_name, server_address)

    print('waiting to receive')
    data, server = sock.recvfrom(4096)

    echoed_message = data.decode('utf-8')
    echoed_message = echoed_message.replace("\\n", "\n")
    print(echoed_message)

finally:
    print('closing socket')
    sock.close()