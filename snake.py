#!/usr/bin/python3
import socket
import sys
import time
print("snakebot v1.0")
ircsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server = input("Host:")
port = input("Port number:")
botnick = input("botnick:")
channel = input("channel:")
exitcode = "bye " + botnick
ircsock.connect((server, port)) 
ircsock.send(bytes("USER "+ botnick +" "+ botnick +" "+ botnick + " " + botnick + "n", "UTF-8")) 
ircsock.send(bytes("NICK "+ botnick +"n", "UTF-8"))
ircsock.send("JOIN "+ channel +"\n")

while 1:    
   text=irc.recv(2040)  
   print text
 if text.find('PING') != -1:
    ircsock.send('PONG ' + text.split() [1] + '\r\n')
 if text.find('!time') != -1:
    ircsock.send('the time is: ' + text.split() [1] + '\r\n')

    
 
