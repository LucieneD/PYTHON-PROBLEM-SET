#THIS PROGRAM WILL COMPUTE THE CHANGE IN VALUE OF A STOCK
print ("What is he purchase price per share")
Pprice = float(input())
print ("What is the current stock price")
Cprice = float(input())
print ("How many shares are you purchasing")
shares = int(input())
Stockvalue = (Cprice - Pprice) * shares
print ("The current value of the stock is", Stockvalue)

