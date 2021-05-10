from socket import *
from options import *
from jim import *
from log.server_log_config import server_logger


def run(args, options_file):
    sock = socket(AF_INET, SOCK_STREAM)  # creates tcp socket
    conf = get_options(args, options_file)
    host = conf['DEFAULT']['HOST']
    port = int(conf['DEFAULT']['PORT'])

    try:
        if not 65535 >= port >= 1024:
            raise ValueError
        sock.bind(('', port))
        sock.listen(5)  # server is waiting for requests;
        print("sever is running")
    except ValueError:
        server_logger.critical('port has to be in [1024 ... 65535]')
        sys.exit(1)

    while True:
        client, addr = sock.accept()
        data = client.recv(1000000)
        if unpack(data):
            print('Message: ', unpack(data), ', was sent by client: ', addr)
            if isinstance(unpack(data), dict):
                server_logger.debug('presence message is correct')
                msg = status_200()
            else:
                msg = status_402()
                server_logger.debug('presence message is incorrect')
            client.send(msg)
            client.close()
        else:
            print('Client message is in wrong format')


if __name__ == '__main__':
    run(sys.argv, "config_server.json")
