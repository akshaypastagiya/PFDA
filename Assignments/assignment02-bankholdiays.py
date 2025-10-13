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
niholidays_date = []

# get bankholidays date from data
for date in niholidays:
    niholidays_date.append(date['date']) 

print(f"Bank holidays date in Northern Ireland are: \n {niholidays_date}")