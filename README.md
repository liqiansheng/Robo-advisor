## Robo-advisor
"""
# for set-up 
1. In your command application, type "pwd" to check your current working direcotry.
2. Change the working directory to where the file is located. In my case, type "cd Desktop/Github/Robo_advisor".
3. Create requirement.txt file to store package names so that it is easier to install in command line application
4. type "conda create -n stock-env python=3.8" and "conda activate stock-env" to activate stock-env environment
5. install all the package required by "pip install -r requirements.txt"
6. test your code by "python app/Robo-advisor.py" 

# User guide
1. Choose the stock you are interest in. You are able to choose multiple at each run. The program will tell you if your code is invalid.
2. Program will confirm your stock input
3. Choose your risk preference. This is the key factor for our recommendation.
4. Program will confirm your answer
5. Program will then record each stock price data as dataframe and store in github Robo-advisor file under "data". Each stock will have their seperate file and name.
6. At the end, the program will print the reasult for each stock containing their symbol, last closing date, latest closing price, recent high price and recent low price. 
7. Finally, program will generate recommendation based on the stock you choose and your risk preference.


"""

