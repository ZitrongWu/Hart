#coding:utf8
import socket
import time
import os
import threading
import argparse

MAX_BYTES = 1024
is_alive = 0

def server(host,port,delay):

    sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    sock.bind((host,port))

    while True:
        #print('test')
        data,addr = sock.recvfrom(MAX_BYTES)
        print('recieve %s:%s' % addr, data.decode('utf8'))



def main():
    #server('0.0.0.0', 5000, 5)
    parse = argparse.ArgumentParser(description='Listen to a port and excute a file')
    parse.add_argument('-H',nargs='?',default='127.0.0.1',const='127.0.0.1')
    parse.add_argument('-P',nargs='?',default=5512,const=5512,type=int)
    parse.add_argument('-D',nargs='?',default=5,const=5,type=int)
    result = parse.parse_args()
    print(result.H,result.P,result.D)
    server(result.H,result.P,result.D)





if __name__=='__main__':
    main()