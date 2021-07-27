user_stockpool = [] # to store stock inputs
while True:
    user_input = input("Please name a stock or cryptocurrency. If you want to skip, please enter Done.")
    if user_input == "Done":
        break
    else:
        user_stockpool.append(user_input)

print(user_stockpool)
    
