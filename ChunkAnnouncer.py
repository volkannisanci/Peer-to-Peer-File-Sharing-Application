import json
import math
import os
import time
from os import listdir
from os.path import isfile, join
from socket import *
import datetime


file = input("Enter the file you want to upload : ")


def divide_five_chunks(file, directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
    c = os.path.getsize(file)
    CHUNK_SIZE = math.ceil(math.ceil(c) / 5)
    cnt = 1
    with open(file, 'rb') as infile:
        divided_file = infile.read(int(CHUNK_SIZE))
        while divided_file:
            name = directory + "/" + file + "_" + str(cnt)
            with open(name, 'wb+') as div:
                div.write(divided_file)
            cnt += 1
            divided_file = infile.read(int(CHUNK_SIZE))
    print(file + " is divided into 5 chunks\nEach chunk is " + str(CHUNK_SIZE) + " bytes")


divide_five_chunks(file, "Chunk_Files")





try:

    d = {}

    file_path = "Chunk_Files/"
    d["files"] = [f for f in listdir(file_path) if isfile(join(file_path, f))]
    chunks = d['files']
    print('{"chunks" :' ,chunks, '}')

    print("Program Started At : " + str(datetime.datetime.now()))
    count = 0

    username = input("Username : ")

    d["username"] = username

    s = socket(AF_INET, SOCK_DGRAM)
    s.connect(("25.255.255.255", 5001))
    ip = s.getsockname()[0].split(".")
    print( "IP Address: " + ip[0] + "." + ip[1] + "." + ip[2] + ".255")
    s.close()
    a = socket(AF_INET, SOCK_DGRAM)
    a.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
    a.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)





    while 1:
        count += 1
        d["files"] = [f for f in listdir(file_path) if isfile(join(file_path, f))]
        print("Announcing for " + str(count) + " times")

        a.sendto(json.dumps(d).encode(), ("25.255.255.255", 5001))
        print("Announce sent at : " + str(datetime.datetime.now()))
        time.sleep(60)
except KeyboardInterrupt:
    print("Exitting.")