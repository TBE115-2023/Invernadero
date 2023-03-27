#Librerias 
import mysql.connector as mysql
import time
import board 
import adafruit_pcf8591.pcf8591 as PCF 
from adafruit_pcf8591.analog_in import AnalogIn
from adafruit_pcf8591.analog_out import AnalogOut

#objeto para la comunicacion I2C
i2c = board.I2C()
pcf = PCF.PCF8591(i2c)

#Variables de manejo de puertos del modulo PCF8591
pcf_in0 = AnalogIn(pcf, PCF.A0)#lectura de luminosidad
pcf_in1 = AnalogIn(pcf, PCF.A1)#lectura de temperatura ambiente 
pcf_in2 = AnalogIn(pcf, PCF.A2)#lectura de sensor de humedad 1 
pcf_in3 = AnalogIn(pcf, PCF.A3)#lectura de sensor de humedad 2
pcf_out = AnalogOut(pcf, PCF.OUT)#Salida analogica, a modo de salida digital

#varibles de calculo
val1= 0
val2= 0
val3= 0
val4= 0

vlux = 0.00
vtemp = 0.00
vh1 = 0.00
vh2 = 0.00

lumi = 0.00
temp = 0.00
phum1= 0.00
phum2= 0.00


#Creacion del objeto mysql y su cursor
db = mysql.connect (host="192.168.1.24", user="leo", passwd="1234", database = "invernadero")
cursor = db.cursor()

#pcf_out.value = 65535
#time.sleep(1)
#pcf_out.value = 0
#time.sleep(0.5)
val1 = pcf_in0.value
vlux = (val1/65535)
vlux = vlux*5
lumi = 10 + ((600-10)/(0.91-4.47))*(vlux-4.47)
#print ("Voltaje de luz :",vlux)
print ("luminosidad :", lumi)
val2 = pcf_in1.value
vtemp = (val2/65535)
vtemp = vtemp*5
temp = 20 + ((54-20)/(4.19-4.60))*(vtemp-4.60)
#print ("Voltaje de temp :",vtemp)
print ("La temperatura es: ",temp,"°")
val3 = pcf_in2.value
vh1  = (val3/65535)
vh1  = vh1*5
phu1 = 0 + ((100-0)/(1.46-3.48))*(vh1-3.48)
#print ("voltaje de hum1 :",vh1)
print ("El porcentaje de humedad 1 :",phu1,"%")
val4 = pcf_in3.value
vh2  = (val4/65535)
vh2  = vh2*5
phu2 = 0 + ((100-0)/(1.46-3.48))*(vh2-3.48)
#print ("voltaje de hum2 :",vh2)
print ("El porcentaje de humedad 2 :",phu2,"%")

#Crecaion del QUERY DE INSERCION
query = "INSERT INTO sensores(sensor1,sensor2,sensor3,sensor4) VALUES(%s,%s,%s,%s)"
#Arreglo de los valores leidos 
valores = (lumi,temp,phu1,phu2)
#inserccion de datos
cursor.execute(query,valores)
db.commit()
#Cerrando las conexiones a la db
cursor.close()
db.close()
print ("Datos almacenados")
