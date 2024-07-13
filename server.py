import socket
import os
from faker import Faker

sock = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)

server_address = os.path.expanduser('~/udp_socket_file')

try:
    os.unlink(server_address)
except FileNotFoundError:
    pass

print('starting up on {}'.format(server_address))

sock.bind(server_address)


while True:
    print('\nwaiting to receive message')

    data, address = sock.recvfrom(4096)

    print('received {} bytes from {}'.format(len(data), address))
    print(data)

    if data:
        fake = Faker()
        name = 'Name : ' + data.decode('utf-8')
        user_address = 'Address : ' +  fake.address()
        text = 'Message : ' + fake.text()
        message = name + '\n' + user_address + '\n' + text
        sent = sock.sendto(message.encode('utf-8'), address)

        print(message)
        print('Sent {} bytes back to {}'.format(sent, address))