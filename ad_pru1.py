import smbus
import time 

address = 0x48
A0 = 0x40
A1 = 0x41
A2 = 0x42
A3 = 0x43
bus = smbus.SMBus(1)
while True:
    bus.write_byte(address,A0)
    value = bus.read_byte(address)
    print ("Temperatura :",value)
    bus.write_byte(address,A1)
    value = bus.read_byte(address)
    print ("Luz :",value)
    time.sleep(2)
        
