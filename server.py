from socket import *
from options import *
from jim import *


def run(args, options_file):
    sock = socket(AF_INET, SOCK_STREAM)  # creates tcp socket
    conf = get_options(args, options_file)
    host = conf['DEFAULT']['HOST']
    port = int(conf['DEFAULT']['PORT'])
    sock.bind(('', port))
    sock.listen(5)  # server is waiting for requests;
    print("sever is running")
    while True:
        client, addr = sock.accept()
        data = client.recv(1000000)
        if unpack(data):
            print('Message: ', unpack(data), ', was sent by client: ', addr)
            msg = status_200()
            client.send(msg)
            client.close()
        else:
            print('Client message is in wrong format')


run(sys.argv, "config_server.json")
