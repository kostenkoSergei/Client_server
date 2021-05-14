import socket
import time
from jim import *
from options import *
from log.client_log_config import client_logger
from log.logger_decorator import Log


@Log('DEBUG')
def create_presence_msg(user_name, status):
    ts = time.time()
    presence_msg = {
        "action": "message",
        "time": ts,
        "type": "status",
        "user": {
            "account_name": user_name,
            "status": status
        }
    }
    # presence_msg = "wrong message format. string instead dict"
    return presence_msg


def send(args, options_file):
    conf = get_options(args, options_file)
    host = conf['DEFAULT']['HOST']
    port = int(conf['DEFAULT']['PORT'])
    try:
        if not 65535 >= port >= 1024:
            raise ValueError
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((host, port))
    except ValueError:
        client_logger.critical('port has to be in [1024 ... 65535]')
        sys.exit(1)
    except socket.error as err:
        print(f"Connection error: {err}")
        sys.exit(2)
    msg = pack(create_presence_msg("Some user", "initial message"))
    sock.send(msg)

    try:
        byte_msg = sock.recv(1024)
        msg = unpack(byte_msg)
        if msg['response'] == 200:
            print(msg)
            client_logger.debug('server answered, status code = 200')
        elif msg['response'] == 402:
            print(msg)
            client_logger.debug('server answered, status code = 402')
        else:
            raise ValueError
    except (ValueError, json.JSONDecodeError):
        client_logger.error('Message decoding error')
    except socket.timeout:
        client_logger.error("Close connection by timeout.")

    if not msg:
        print("No response")

    sock.close()
    print("client close...")


if __name__ == '__main__':
    send(sys.argv, "config_client.json")
