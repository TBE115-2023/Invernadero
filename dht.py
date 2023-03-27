import time 
import adafruit_dht 
import RPi.GPIO as GPIO
import board

dht = adafruit_dht.DHT11(board.D5, use_pulseio=False)
temp = dht.temperature
hum = dht.humidity

print (temp)
time.sleep (1)
print (hum)
time.sleep(1)
