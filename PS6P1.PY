#THIS PROGRAM WILL COMPUTE THE EXTENDED PRICE OF A WIDGET USING QUANTITY
print ("Enter quantity of widget")
qty = float(input())
if qty > 10000:
  uprice = 10.00
  if qty >= 5000 and qty <=10000:
    uprice = 20.00 
else: uprice = 30.00

extprice = round (qty*uprice, 2)
tax = round (extprice*0.07, 2)
total= round (uprice+tax, 2)
print ("The unit price based on this quanitty is $" + str(uprice))
print ("The extend price based on quantity enetered is $" + str(extprice))
print ("The amount of tax on this item is $" + str(tax))
print ("The total price of the item is $" + str(total))
