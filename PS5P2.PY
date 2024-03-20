#THIS PROGRAM WILL DETERMINE UNIT PRICE OF AN ITEM
print ("Enter the name of the item")
item = input()
print ("Enter the quantity of the item")
quantity = int(input())
A = 10.00
B = 20.00
if item == A: 
  unitprice = 10.00
else :
  unitprice = 20.00


total = quantity * unitprice
print ("The unit price is" + str(unitprice))

print ("The total price of " + item + "is" + str(total))
