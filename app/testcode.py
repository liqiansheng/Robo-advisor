import requests
import json
from pprint import pprint
from getpass import getpass

user_stockpool = [] # to store stock inputs
api_key = input("Please input your API key:")

# Ask user which stock they are interested in
while True:
    user_input = input("Please name a stock or cryptocurrency. If you want to skip, please enter Done.")
    numbers = sum(c.isdigit() for c in user_input)
    if user_input.upper() == "DONE":
        break
    elif len(user_input) <2 or len(user_input)>5 or numbers != 0:
        print("Oh, expecting a properly-formed stock symbol like 'MSFT'. Please try again.")
    else:
        user_stockpool.append(user_input.upper())

print(user_stockpool)
    
# ask for their risk preference 
while True:
  user_input1 = input("Do you consider yourself risk-averse?(yes/no)")
  if user_input1.upper() != "YES" and user_input1.upper() != "NO":
    print("Invalid input! Please choose either yes or no.")
  else:
    break


# import data
for stock in user_stockpool:
  url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={stock}&apikey={api_key}"
  response = requests.get(url)
  parsed_response = json.loads(response.text)
  print(type(parsed_response))
  pprint(parsed_response)
  if "Error Message" in parsed_response: #print error message if symbol is incorret
    print("Sorry, couldn't find any trading data for that symbol. please check your input and rerun the programy.\n\n\n")
   
  
  

  
  