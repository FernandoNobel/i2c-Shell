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
    time.sleep(1)
    #while True:
    #c = bus.read_byte(address)
    # c = bus.read_i2c_block_data(address,0,256)
    with SMBus(1) as bus:
        # Read 64 bytes from address 80
        msg = i2c_msg.read(address, 1024)
        bus.i2c_rdwr(msg)
        print(msg)


    #c = bus.read_word_data(address)
    #print(c)
    #c = chr(c)
    #print(c)
    #if c == '\0':
        #break
    #ans += c
    #print(c)

    print(ans)
    return ans

while True:
    print(">>: ", end='')
    line = input()

    if line == "exit":
        break

    sendCommand(line)

    ans = reciveResponse()
    print("<<: " + ans)
