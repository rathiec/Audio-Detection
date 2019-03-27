# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 12:36:41 2019

@author: Rathi
"""

import SimpleHTTPServer
import SocketServer
import sys

PORT_NUMBER = int(sys.argv[1])

try:
    handler = SimpleHTTPServer.SimpleHTTPRequestHandler
    server = SocketServer.TCPServer(('', PORT_NUMBER), handler)
    
    server.serve_forever()
    
except KeyboardInterrupt:
    server.socket.close()
 