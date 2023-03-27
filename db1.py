import mysql.connector as mysql
import time
s1 = 33.34
s2 = 54.56
s3 = 3.12
s4 = 1.09
db = mysql.connect (host="192.168.1.35", user="root", passwd="1234", database="invernadero")
cursor =  db.cursor()
query = "INSERT INTO sensores(sensor1,sensor2,sensor3,sensor4) VALUES (%s,%s,%s,%s)"
valores = (s1,s2,s3,s4)
cursor.execute(query,valores)
db.commit()
cursor.close()
db.close()
print("mysql")
