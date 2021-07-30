import requests
import json
from pprint import pprint
from getpass import getpass
from pandas import DataFrame
import datetime
from dotenv import load_dotenv
import os

load_dotenv()

user_stockpool = [] # to store stock inputs
api_key = os.getenv("ALPHAVANTAGE_API_KEY")
time_now = datetime.datetime.now()

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
for stock in user_stockpool:
  print("You chose:", stock)
    
# ask for their risk preference 
while True:
  user_input1 = input("Do you consider yourself risk-averse?(yes/no)")
  if user_input1.upper() != "YES" and user_input1.upper() != "NO":
    print("Invalid input! Please choose either yes or no.")
  else:
    break
print("You said:",user_input1.upper())


# import data
for stock in user_stockpool:
  url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={stock}&apikey={api_key}"
  response = requests.get(url)
  parsed_response = json.loads(response.text)
  
  
  if "Error Message" in parsed_response: #print error message if symbol is incorret
    print("Sorry, couldn't find any trading data for that symbol. please check your input and rerun the programy.\n\n\n")
  else:  
    stock_df = DataFrame(parsed_response["Time Series (Daily)"])
    stock_df_transpose = stock_df.transpose()
    stock_df_transpose.drop(columns=["5. adjusted close","7. dividend amount", "8. split coefficient"],inplace=True)
    stock_df_transpose.columns = ['open', 'high', 'low', 'close', 'volume']
    
    stock_df_transpose['timestamp']= stock_df_transpose.index
    stock_df_transpose.index = range(len(stock_df_transpose))
    stock_df_transpose = stock_df_transpose[['timestamp','open', 'high', 'low', 'close', 'volume']]
    stock_df_transpose.to_csv(f'data/{stock}_Price.csv',index=False)

    # Calculation
    stock_date = list(parsed_response["Time Series (Daily)"])
    stockclose_info = list(parsed_response["Time Series (Daily)"].items())
    latest_closeprice = float(stockclose_info[0][1]["4. close"])
    dollar_closeprice = '${:,.2f}'.format(latest_closeprice)
    latest_highprice = float(stockclose_info[0][1]["2. high"])
    dollar_highprice = '${:,.2f}'.format(latest_highprice)
    latest_lowprice = float(stockclose_info[0][1]["3. low"])
    dollar_lowprice = '${:,.2f}'.format(latest_lowprice)
    recent_highprice = max([float(x) for x in stock_df_transpose["high"].tolist()])
    dollar_recenthighprice = '${:,.2f}'.format(recent_highprice)
    recent_lowprice = min([float(x) for x in stock_df_transpose["low"].tolist()])
    dollar_recentlowprice = '${:,.2f}'.format(recent_lowprice)


    # Output
    print("-------------------------")
    print("Stock:", parsed_response["Meta Data"]["2. Symbol"])
    print("-------------------------")
    print("REQUESTING STOCK MARKET DATA...")
    print("REQUEST AT:%s:%s:%s" % (time_now.hour, time_now.minute, time_now.second),"ON %s/%s/%s" % (time_now.day, time_now.month, time_now.year))
    print("-------------------------")
    print("LATEST DAY:",stock_date[0])
    print("LATEST CLOSE:", dollar_closeprice)
    print("RECENT HIGH:",dollar_recenthighprice)
    print("RECENT LOW:",dollar_recentlowprice)
    print("-------------------------")

    # RECOMMENDATION ALGORITHM
    if latest_highprice == recent_highprice and user_input1.upper() == "NO":
      print("RECOMMENDATION: BUY!")
      print("RECOMMENDATION REASON: PRICE WILL KEEP CLIMBING")
    
    elif latest_closeprice >= 1.1 * recent_lowprice and user_input1.upper() == "YES":
      print("RECOMMENDATION: BUY")
      print("RECOMMENDATION REASON: PRICE WILL BOUNCE BACK!")
    
    else:
      print("RECOMMENDATION: STAY CALM, NOT THE RIGHT TIMING")
      print("RECOMMENDATION REASON: THE STOCK PRICE IS UNPREDITABLE")
  
    
    
    

    


  
  

  
  