import mysql.connector
import csv
connection=mysql.connector.connect(host='localhost',user='root',password='Practicemakesamanperfect@7',database='cropprediction')
cursor=connection.cursor()
cursor.execute("select * from samplecopy")
data=cursor.fetchall()
# print(data)
#continue continue. . . :)
with open('data.csv','w') as csvfile:
    #sc = new java.lang.scanner(system.in)
    csvwriter = csv.writer(csvfile) #parameters
#object=package.class.parameter
    csvwriter.writerows(data)

