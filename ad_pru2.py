import time
import board 
import adafruit_pcf8591.pcf8591 as PCF 
from adafruit_pcf8591.analog_in import AnalogIn
from adafruit_pcf8591.analog_out import AnalogOut
i2c = board.I2C()
pcf = PCF.PCF8591(i2c)

pcf_in0 = AnalogIn(pcf, PCF.A0)
pcf_in1 = AnalogIn(pcf, PCF.A1)
pcf_in2 = AnalogIn(pcf, PCF.A2)
pcf_in3 = AnalogIn(pcf, PCF.A3)
pcf_out = AnalogOut(pcf, PCF.OUT)

while True:
    print ("valor a enviar: ", 65535)
    pcf_out.value = 65535
    time.sleep(1)
    print ("valor a enviar:", 0)
    pcf_out.value = 0
    time.sleep(0.5)
    val1 = pcf_in0.value
    vlux = (val1/65535)
    vlux = vlux*5
    print ("Voltaje de luz :",vlux)
    val2 = pcf_in1.value
    vtemp = (val2/65535)
    vtemp = vtemp*5
    print ("Voltaje de temp :",vtemp)
    val3 = pcf_in2.value
    vh1  = (val3/65535)
    vh1  = vh1*5
    print ("voltaje de hum1 :",vh1)
    val4 = pcf_in3.value
    vh2  = (val4/65535)
    vh2  = vh2*5
    print ("voltaje de hum2 :",vh2)
    time.sleep(5)
