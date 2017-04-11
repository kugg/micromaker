#!/usr/bin/python
"""Read an ipaddress and port translate in to FTP PORT command syntax."""
import sys

def ftpify(ip, port):
    """Convert ipaddr and port to FTP PORT command."""
    iplist = ["","","",""]
    
    for octet in range(0, 4):
        iplist[octet] = ip.split('.')[octet]

    port_hex = hex(int(port)).split('x')[1]

    big_port = int(port_hex[:-2], 16)
    little_port = int(port_hex[-2:], 16)
    iplist.append(str(big_port))
    iplist.append(str(little_port))
    return iplist

if __name__ == "__main__":
    ip = sys.argv[1]
    port = sys.argv[2]
    portlist = ftpify(ip, port)
    print("%0APORT%20{}".format(",".join(portlist)))
