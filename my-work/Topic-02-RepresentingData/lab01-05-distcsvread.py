# This program is to read data.csv CSV file as disctionary object
# in that csv calculate the average age
# Author: Akshay Pastagiya
# to read csv file will be using csv function
# for csv function refer following link
# https://docs.python.org/3/library/csv.html
# https://realpython.com/python-csv/

import csv
filename = "data.csv"
datadir = "..\\..\\data\\"

with open (datadir + filename, "rt") as fp:
    reader = csv.DictReader(fp,delimiter=",")
    linecount = 0
    total=0
    for line in reader:
        total += int(line["age"]) # there are 3 the 1st one is ID 2nd one is Age and 3rd one is name here we need to get data of age for avg calculaten and age is 2nd so, it will 0, 1 that wht it 1 here
        linecount += 1
    print(f"average of the age is {total/(linecount)}")