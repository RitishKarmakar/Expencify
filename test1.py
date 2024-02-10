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
