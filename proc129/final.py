import csv

dataset1 =[]
dataset2 = []

with open("data1.csv","r",encoding='utf8') as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        dataset1.append(row)

with open("data1_sorted.csv","r",encoding='utf8') as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        dataset2.append(row)

header1 = dataset1[1]
star_data1 = dataset1[1:]

header2 = dataset2[2]
star_data2 = dataset2[2:]

headers = header1+header2
star_data = []

for index,datarow in enumerate(star_data1):
    star_data.append(star_data+star_data2)

with open("final.csv","w",encoding="utf8", errors='ignore') as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(star_data)