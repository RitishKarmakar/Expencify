import csv
import matplotlib.pyplot as plt

csv_file_path = 'data.csv'
data_list=[]
# Open the CSV file
with open(csv_file_path, 'r') as file:
    # Create a CSV reader object
    csv_reader = csv.reader(file)

    # Iterate through each row in the CSV file
    for row in csv_reader:
        # Each row is a list where each element represents a column value
        data_list.append(row)
x = []
y=[]
plt.figure(figsize=(10,6))
for items in data_list:
    if items[0]=="Dist Code":
        continue
    if items[4]=="Durg":
        x.append(items[1])
        y.append(items[7])
# plt.scatter(x,y)
# plt.plot(x,y)
plt.hist(y,bins=30,color="green",edgecolor="black")
plt.legend()
plt.show()


