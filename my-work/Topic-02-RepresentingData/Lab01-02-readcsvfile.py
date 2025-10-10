# This program is to read data.csv CSV file
# Author: Akshay Pastagiya
# to read csv file will be using csv function
# for csv function refer following link
# https://docs.python.org/3/library/csv.html
# https://realpython.com/python-csv/

import csv
filename = "data.csv"
datadir = "..\\..\\data\\"

with open (datadir + filename, "rt") as fp:
    reader = csv.reader(fp,delimiter=",")
    for line in reader:
        print(line)