# This program is to read data.csv CSV file
# Seperate the header as a 1st line
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
    linecount = 0
    for line in reader:
        if linecount == 0:
            print(f"{line}\n----------------")
        else:
            print(line)
        linecount += 1
            