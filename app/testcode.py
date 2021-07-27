user_stockpool = [] # to store stock inputs
while True:
    user_input = input("Please name a stock or cryptocurrency. If you want to skip, please enter Done.")
    numbers = sum(c.isdigit() for c in user_input)
    if user_input == "Done":
        break
    elif len(user_input) <2 or len(user_input)>5 or numbers != 0:
        print("Oh, expecting a properly-formed stock symbol like 'MSFT'. Please try again.")
    else:
        user_stockpool.append(user_input)

print(user_stockpool)
    
