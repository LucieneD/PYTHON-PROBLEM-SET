#THIS PROGRAM WILL CALCULATE THE BREAK EVEN POINT OF A COMPANY
print ("What is the fixed cost of the item")
fixed = float(input())
print ("What is the price per unit")
unit = float(input())
print ("What is the cost per unit")
cost = float(input())
Breakeven = ((cost - unit) / fixed)
print ("The break even point is", Breakeven)
