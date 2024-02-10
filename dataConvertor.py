import mysql.connector
db = mysql.connector.connect(host="localhost", user = 'root',password='root',database = 'cropprediction')

x=open("precipitation.txt",'r')
data = x.readlines()
print(data)
empty_string=""
row=[]
table=[]
for i in data:
    for j in i:
        if j!="\t" and j!="\n":
            empty_string+=j
        elif j=="\t" or j=="\n":
            row.append(empty_string)
            empty_string=""
    table.append(row)
    row=[]
print(table)
cursor = db.cursor()

# for i in data:
#     if i=="\n":
#         print("\n")
table.pop()

for i in table:
    print(i)
    command = "update samplecopy set precipitation = {},soil_type=\"{}\",sunlight={},pest_and_disease=\"{}\" where district = \"{}\""
    

    cursor.execute(command.format(i[1],i[2],i[3],i[4],i[0]))
    db.commit()
# print(data)
# x = open("commands.txt",'w')
# x.write("create table samplecopy(slno int primary key,state varchar(255),district varchar(255),precipitation float);\ninsert into samplecopy values")
# #x.write("Ritish Loves Queenie \nshe knows it.")
# for i in data:
#     j=str(i)+",\n"
#     x.write(j)
#
#
# x.close()


