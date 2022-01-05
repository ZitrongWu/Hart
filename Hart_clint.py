#coding:utf8
import argparse
import socket
import time

def client(host,port,delay):
    udp_sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    while True:
        #udp_sock.connect((host,port))
        udp_sock.sendto('2333'.encode('ascii'),(host,port))
        #udp_sock.send('2333'.encode('ascii'))
        time.sleep(delay)


def main():    
    parse = argparse.ArgumentParser(description="Sent a message to a host")
    parse.add_argument('-H',nargs='?',default='firstalley.cn',const='firstalley.cn')
    parse.add_argument('-P',nargs='?',default=5512,const=5512,type=int)
    parse.add_argument('-D',nargs='?',default=3,const=3,type=int)
    result = parse.parse_args()
    print(result.H,result.P,result.D)
    client(result.H,result.P,result.D)


if __name__=='__main__':
    main()