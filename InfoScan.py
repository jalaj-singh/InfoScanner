#!/usr/bin/python

from socket import *
import optparse
from threading import *

def connScan(tgtHost, tgtPort):
    global sock
    try:
        sock = socket(AF_INET, SOCK_STREAM)
        sock.connect((tgtHost,tgtPort))
        print("[-] The Port {}/tcp Open".format(tgtPort))
    except:
        print("[-] The Port {}/tcp Closed".format(tgtPort))
    finally:
        sock.close()

def portScan(tgtHost, tgtPorts):
    global tgtIP
    try:
        tgtIP = gethostbyname(tgtHost)
    except:
        print("Unknown Host {}".format(tgtHost))
    try:
        tgtName = gethostbyaddr(tgtIP)
        print("[+] Scan Results For :",tgtName[0])
    except:
        print("[+] Scan Results For :", tgtIP)
    setdefaulttimeout(1)
    for tgtPort in tgtPorts:
        t = Thread(target=connScan, args=(tgtHost,int(tgtPort)))
        t.start()


def main():
    parser = optparse.OptionParser("Usage of program :, -H <Target Host IP or Name> -p <target Port>")
    parser.add_option('-H', dest='tgtHost',type='string', help='Specify target Host')
    parser.add_option('-p', dest='tgtPort', type='string', help='Specify target Port Or Comma Seperated Ports')
    (options, args) = parser.parse_args()
    tgtHost = options.tgtHost
    tgtPorts = str(options.tgtPort).split(',')
    if (tgtHost == None) | (tgtPorts[0] == None):
        print(parser.usage)
        exit(0)
    portScan(tgtHost,tgtPorts)



if __name__ == '__main__':
    main()
