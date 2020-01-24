import csv

with open('employees.csv') as f_object:
    f_object = csv.reader(f_object)
    data = [row for row in f_object]


print(data[1])