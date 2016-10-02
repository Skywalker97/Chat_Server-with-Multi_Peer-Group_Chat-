from socket import *
import os, sys

def connect(tcpclientsoc, fp, PORT, ip):

    try:
        tp = open('log/last_server.txt', 'r')
        HOST = tp.readline()
        ADDR = (HOST, PORT)
        check = tcpclientsoc.connect(ADDR)
        if (not check):
            # os.system("clear")
            fp.write('\nConnected to server: [%s: %s]' % ADDR)
            print 'Connected to server: [%s: %s]' % ADDR
            tp.close()
            return True

    except:
        for i in range(50, 250):
            HOST = ip + str(i)
            ADDR = (HOST, PORT)
            fp.write('Checking For Server on Address: [%s: %s] ' % ADDR,)
            fp.flush()
            # print 'Checking For Server on Address: [%s: %s] ' % ADDR,
            try:
                timeout(10)
                check = tcpclientsoc.connect(ADDR)
                timeout(None)
                if (not check):
                    # os.system("clear")
                    fp.write('\nConnected to server: [%s: %s]' % ADDR)
                    tp = open('log/last_server\'s.txt', 'w+')
                    tp.write(HOST)
                    tp.close()
                    print 'Connected to server: [%s: %s]' % ADDR
                    # my_name = uname()[1]
                    # tcpclientsoc.send(my_name)
                    return True
            except:
                fp.write('Didn\'t find server\n')
                fp.flush()
                # print 'Didn\'t find server'

    finally:
        fp.write('\nNo Online Server Found')
        return False