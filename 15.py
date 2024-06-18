#csv file

import csv

file=input("Enter file name:")
sample=open(file,'r')
f=csv.reader(sample)

for str in f:
    print(str)