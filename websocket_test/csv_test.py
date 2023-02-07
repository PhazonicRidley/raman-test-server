import csv
import time

data = None
with open("small/people.csv") as f:
    data = f.readlines()

for row in data:
    print(row)
with open("test.csv", 'w') as f:
    f.writelines(data)