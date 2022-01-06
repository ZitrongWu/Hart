#coding:utf8
import socket
import time
import os
import threading
import argparse
from Server_list import Server_list
MAX_BYTES = 1024
lock = threading.Lock()

def server(host,port):

    sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    sock.bind((host,port))

    while True:
        #print('test')
        data,addr = sock.recvfrom(MAX_BYTES)
        with lock:
            servers.active(data.decode('utf8'))
        print('recieve %s:%s' % addr, data.decode('utf8'))

def timesup():
    while True:
        time.sleep(delay)
        with lock:
            servers.check()

servers=Server_list()

def main():
    #server('0.0.0.0', 5000, 5)
    global delay
    parse = argparse.ArgumentParser(description='Listen to a port and excute a file')
    parse.add_argument('-H',nargs='?',default='0.0.0.0',const='0.0.0.0')
    parse.add_argument('-P',nargs='?',default=0,const=0,type=int)
    parse.add_argument('-D',nargs='?',default=3600,const=3600,type=int)
    result = parse.parse_args()
    print(result.H,result.P,result.D)
    delay = result.D
    client = threading.Thread(target=timesup)
    client.setDaemon(True)
    client.start()

    server(result.H,result.P)





if __name__=='__main__':
    main()