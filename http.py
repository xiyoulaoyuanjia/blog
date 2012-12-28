#!/usr/bin/python
'''
      File      : redirect.py
      Author    : Mike
      E-Mail    : Mike_Zhang@live.com
'''
import socket,os
bufLen = 4*1024
sock1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
sock1.bind(('10.210.48.143', 8000))  
sock1.listen(5)  
sock2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
#sock2.connect(('localhost', 8002))  
while True:
        connection,address = sock1.accept()  
        buf = connection.recv(bufLen)  
        #print buf            
 #       sock2.send(buf)  
 #       connection.send(sock2.recv(bufLen))
        connection.send("ggggg")
        connection.close()
