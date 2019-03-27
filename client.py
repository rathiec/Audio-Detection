# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 11:10:37 2019

@author: Rathi
"""

import socket
port = 50010
server_address = ('iot.lukefahr.org', port)
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
data = b'This is the message.'
s.sendto(data, server_address)
s.close()
