#!/usr/bin/python3
import socket
import sys
import time
print("snakebot v1.0")
ircsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server = input("Host:")
port = input("Port number:")
nick = input("botnick:")
channel = input("channle:")

