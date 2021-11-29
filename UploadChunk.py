from datetime import *
import json
import os
import math
import socket
from threading import *


def func_ip1():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("25.255.255.255", 5001))
    ip = s.getsockname()[0]
    s.close()
    return ip

def own_ip():
    #Enter your own Hamachi IPv4 address
    return "25.48.38.203"


def server(ip):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((ip, 8000))
    sock.listen(50)
    print("Server has been started.")
    while True:
        conn, info = sock.accept()
        Thread(target=send, args=(conn, info)).start()


def write_log(message, log_file_name):
    with open(log_file_name, "a") as log:
        log.write(message)


def send(conn, clientInfo):
    try:
        while True:
            data = conn.recv(4096)
            if data:
                fileName = "Chunk_Files/" + json.loads(data.decode())["filename"]
                with open(fileName, "rb") as f:
                    conn.send(f.read(os.path.getsize(fileName)))
                    write_log(str(datetime.now()) + "," + clientInfo[0] + "," + fileName + "\n", "Success.log")
                    break
            else:
                break
    except:
        write_log(str(datetime.now()) + ", Error has been occured.", "Fail.log")
    finally:
        conn.close()



if __name__ == '__main__':
    server(own_ip())
