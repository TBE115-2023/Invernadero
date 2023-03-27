import Adafruit_DHT as dht

sens= dht.DHT11

h,t = dht.read_retry (sens,5)
print ("T= ",t," H= ",h)
