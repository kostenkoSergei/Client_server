import socket
import time
from jim import *
from options import *


def create_presence_msg(user_name, status):
    ts = time.time()
    presence_msg = {
        "action": "presence",
        "time": ts,
        "type": "status",
        "user": {
            "account_name": user_name,
            "status": status
        }
    }
    return presence_msg


def send(args, options_file):
    conf = get_options(args, options_file)
    host = conf['DEFAULT']['HOST']
    port = int(conf['DEFAULT']['PORT'])
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((host, port))
    except socket.error as err:
        print(f"Connection error: {err}")
        sys.exit(2)
    msg = pack(create_presence_msg("Some user", "initial message"))
    sock.send(msg)

    try:
        msg = sock.recv(1024)
        print(unpack(msg))
    except socket.timeout:
        print("Close connection by timeout.")

    if not msg:
        print("No response")

    sock.close()
    print("client close...")


send(sys.argv, "config_client.json")
