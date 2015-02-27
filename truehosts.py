#!/usr/bin/env python

import subprocess, socket

def main():
    with open("hosts", "r") as f:
        for l in f:
            l = l.strip()

            if not l or l.startswith('#'):
                print (l)
                continue

            (ip, host) = l.split('\t')

            try:
                ip = socket.gethostbyname(host)
                print ("%s\t%s" %(ip, host))
            except Exception as e:
                pass

if __name__ == "__main__":
    socket.setdefaulttimeout(5)
    main()
