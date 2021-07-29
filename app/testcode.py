user_stockpool = [] # to store stock inputs

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
print(user_input1)
