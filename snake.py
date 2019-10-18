#!/usr/bin/python3
import socket
import sys
import time

ircsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server = 'chat.freenode.com'
port = 6697
nick = 'snakebot'
channel = '#snake'

