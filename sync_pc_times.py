#! /usr/bin/env python

# Run this file on Slave PC which is on the same network as the Master PC and with '192.168.0.2' network ID, so as to fetch it's time and set it on the Slave PC.

from subprocess import Popen, PIPE

if __name__=='__main__':
 tmp = Popen(['ssh', 'isera2@192.168.0.2', 'date'], stdout=PIPE)
 print tmp
 print type(tmp)
 tmp_1 = tmp.communicate()
 print tmp_1
 print tmp_1[0][:-1]
 print type(tmp_1)

