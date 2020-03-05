#!/usr/bin/env python3

from smbus2 import SMBus, i2c_msg
import time

# for RPI version 1, use "bus = smbus.SMBus(0)"
bus = SMBus(1)

# This is the address we setup in the turbidostat.
address = 0x42

def sendCommand(line):
    for c in line:
        bus.write_byte(address, ord(c))
    bus.write_byte(address, ord('\0'))
        
def reciveResponse():
    ans = ''
    time.sleep(0.1)

    with SMBus(1) as bus:
        msg = i2c_msg.read(address, 128)
        bus.i2c_rdwr(msg)

    return msg.__str__()

while True:
    print(">>: ", end='')
    line = input()

    if line == "exit":
        break

    sendCommand(line)

    msg = reciveResponse()
    print( msg.split("ÿ",1)[0] )
