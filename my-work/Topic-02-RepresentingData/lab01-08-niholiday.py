# This program is to read the json file from internet
# This will display the 1st holiday in northen ireland
# Aurthor: Akshay Pastagiya
# to run this program required to install pip install requests comaand 1st to install requests library
# for referance follow https://requests.readthedocs.io/en/latest/

import requests  
url =" https://www.gov.uk/bank-holidays.json" 
response = requests.get(url, verify=False) 
data = response.json() 
print(data['northern-ireland']['events'][0]) 
