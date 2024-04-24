def calcextprice(qty, price):
  total = qty*price
  if total > 10000.00:
    total = total- (total*0.10)
  return total 

sumtotal= 0
loop = input("Do you want to loop? If yes, enter 'Y'")
while loop == 'Y':
  qty = float(input("Enter quantity"))
  price = float(input("Enter unit price"))
  extprice = calcextprice(qty, price)
  print ("The total quantity of your item is" + str(qty))
  print ("The unit price of your item is" + str(price))
  print ("The extended price of your item is" + str(extprice))
  sumtotal = sumtotal + extprice
  loop = input("Do you want to loop? If yes, enter 'Y'")

print ("The sum of all extended prices is" + str(sumtotal))