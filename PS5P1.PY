#this program will compute the extended price of an item using the quantity only
print ("Enter quanity")
quantity = float(input())
unitprice = 3.00 if quantity >= 1000 else 5.00 
extendedprice = quantity*unitprice
tax = extendedprice*0.07
toalprice = extendedprice+tax
print (" For the quantity of" + str(quantity))
print ("your unit price is" + str(unitprice))
print ("your extended price is" + str(extendedprice))
print ("your tax is " + str(tax))
print ("your total price is" + str(toalprice))