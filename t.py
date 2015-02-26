#!/usr/bin/env python

import subprocess

def getIP(hostname):
    p = subprocess.Popen("gethostip -d %s" % (hostname), stdout=subprocess.PIPE, stderr=open("/dev/null", "r"), shell=1)  
    res = p.stdout.readlines()

    if len(res):
        return res[0].strip()
    else:
        raise RuntimeError("unknown host")

def main():
    with open("hosts", "r") as f:
        for l in f:
            l = l.strip()

            if not l or l.startswith('#'):
                print (l)
                continue

            (ip, host) = l.split('\t')

            try:
                ip = getIP(host)
                print ("%s\t%s" %(ip, host))
            except RuntimeError as e:
                pass

if __name__ == "__main__":
    main()
