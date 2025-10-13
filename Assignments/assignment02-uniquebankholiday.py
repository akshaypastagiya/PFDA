# This program is to read the json file from internet
# This will display the holiday in northen ireland
# Also display uniq holidays to northen ireland
# Aurthor: Akshay Pastagiya
# to run this program required to install pip install requests comaand 1st to install requests library
# for referance follow https://requests.readthedocs.io/en/latest/

import requests  
url =" https://www.gov.uk/bank-holidays.json" 

#get bank holiday data from the url
response = requests.get(url, verify=False) 
data = response.json() 

#from data get the holidays of northern ireland
niholidays = data['northern-ireland']['events']

#from data get the holidays of england-and-wales
engholidays = data['england-and-wales']['events']

#from data get the holidays of scotland
scoholidays = data['scotland']['events']

# get unique bankholidays date for Northen Ireland
niholidays_uniquedate = []
for nidate in niholidays:
    for engdate in engholidays:
        if engdate['date'] == nidate['date']:
            datenotunique = True
            break
        else:
            datenotunique = False
    if datenotunique == False:
        for scodate in scoholidays:
            if scodate['date'] == nidate['date']:
                datenotunique = True
                break
            else:
                datenotunique = False
    if datenotunique == False:
        niholidays_uniquedate.append(nidate['date'])

print(f"Unique Bank holidays date of Northern Ireland are: \n {niholidays_uniquedate}")