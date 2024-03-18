#this program will compute investment in stock
(print)("Enter stock ticker you are investing in")
ticker = input()
(print) ("enter the amount of shares you would like to buy")
shares = float(input())
(print) ("enter the price per share")
price = float(input())
invested = shares*price
(print) ("Your investment into"  +ticker +  "is"  +  str(invested))