import datetime
import json
import os
import platform
from socket import *


d = {}

try:
    f = open("Users.txt", "a")
    f.close()
    print("Program Started At : " + str(datetime.datetime.now()))
    s = socket(AF_INET, SOCK_DGRAM)
    s.connect(("25.255.255.255", 5001))
    ip = s.getsockname()[0].split(".")
    my_ip = s.getsockname()[0]
    s.close()
    test = ip[0] + "." + ip[1] + "." + ip[2] + ".255"
    print(test)
    sock = socket(AF_INET, SOCK_DGRAM)

    # Enter your own Hamachi IPv4 address
    sock.bind(("25.48.38.203", 5001))

    while 1:
        msg, addr = sock.recvfrom(4096)
        print("Received a packet at : " + str(datetime.datetime.now()))
        recv_ip, _ = addr
        if recv_ip != my_ip or 1:
            dat = json.loads(str(msg.decode()))
            try:
                for file in dat["files"]:
                    d[file] = recv_ip
                for key in d:
                    print("Received Username - " + dat["username"])
                with open("Users.txt", "w") as f:
                    f.write(json.dumps(d))
                    print("Users.txt has been updated")
            except:
                print("Error occured.")
except KeyboardInterrupt:
    print("Exitting")