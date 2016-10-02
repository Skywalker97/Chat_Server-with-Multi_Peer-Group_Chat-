from socket import *
import sys, os, select

def start_chat(tcpclientsoc):
    RECV_BUF = 1024
    while 1:
        socket_list = [sys.stdin, tcpclientsoc]
        read_sockets, write_sockets, error_sockets = select.select(socket_list, [], [])
        for sock in read_sockets:
            if sock == tcpclientsoc:
                data = sock.recv(RECV_BUF)
                if not data:
                    print '\nDisconnected from chat server'
                    sys.exit()
                else:
                    sys.stdout.write(data)
                    sys.stdout.write(">")
                    sys.stdout.flush()
            else:
                msg = sys.stdin.readline()
                tcpclientsoc.send(msg)
                sys.stdout.write(">")
                sys.stdout.flush()