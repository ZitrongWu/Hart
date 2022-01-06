#coding:utf8
import argparse
import socket
import time

def client(host,port,delay,massage):
    udp_sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    udp_sock.sendto(massage.encode('utf8'),(host,port))
    while True:
        #udp_sock.connect((host,port))
        udp_sock.sendto('Server online!'.encode('utf8'),(host,port))
        #udp_sock.send('2333'.encode('ascii'))
        time.sleep(delay)


def main():    
    parse = argparse.ArgumentParser(description="Sent a message to a host")
    parse.add_argument('-H',nargs='?',default='localhost',const='localhost')
    parse.add_argument('-P',nargs='?',default=0,const=0,type=int)
    parse.add_argument('-D',nargs='?',default=60,const=60,type=int)
    parse.add_argument('-M',nargs='?',default="",const="")
    result = parse.parse_args()
    print(result.H,result.P,result.D)
    client(result.H,result.P,result.D,result.M)


if __name__=='__main__':
    main()