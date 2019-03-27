# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 11:25:37 2019

@author: Rathi and Kriti
"""

import librosa
import socket
import struct
import numpy as np
import sys

port = int(sys.argv[1])
s = socket.socket( socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
s.bind( ('0.0.0.0', port))
raw, addr = s.recvfrom(64000)

audio_data = struct.unpack('<' + 'f'*int(len(raw)/4), raw)

audio = np.array(audio_data, dtype = np.float)

librosa.output.write_wav("raw.wav", audio, 16000)

N = 10

for i in range(len(audio)):
    audio[i] = sum(audio[i- N:i])/N

audio2 = np.array(audio_data, dtype = np.float)

librosa.output.write_wav("filter.wav", audio2, 16000)

xs2 = []

for volt in audio2:
    xs2.append(volt**2)
    
mean_square = sum(xs2)/len(xs2)

threshold = 2.7

if mean_square >= threshold:
    s.sendto(b'440Hz',('45.16.202.216',8888))
else:
    s.sendto(b'no440Hz',('45.16.202.216',8888))
