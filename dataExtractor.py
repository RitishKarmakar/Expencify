#wap to extract data from mysql
import mysql.connector
db = mysql.connector.connect(host="localhost",user="root",password="root",database="cropprediction")
cursor=db.cursor()
cursor.execute("select*from samplecopy")
x = cursor.fetchall()
for i in x:
    print(i)