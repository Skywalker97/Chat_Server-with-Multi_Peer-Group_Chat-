import My_ip, startchat, connection
from socket import *
import os, sys, platform

tcpclientsoc = socket(AF_INET, SOCK_STREAM)

ip = My_ip.local_ip_splited()

print My_ip.my_local_ip()

if not os.path.exists('log'):
        os.makedirs('log')

fp = open('log/tcplog.txt', 'w+')

if not fp:
    print 'cant open file'
print 'WAITING FOR A CONNECTION'

connection.connect(tcpclientsoc, fp, 2300, ip)

fp.close()

startchat.start_chat(tcpclientsoc)

tcpclientsoc.close()