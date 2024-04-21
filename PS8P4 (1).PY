#open text file
f = open("PS8P4.txt", "r")
totalorders = 0
extpricetotal = 0
average = 0
item = f.readline().rstrip('\n')
#loop until the last item reads
while item != "":
  qty= float(f.readline().rstrip('\n'))
  price = int(f.readline().rstrip('\n'))
  item = f.readline().rstrip('\n')
  extprice = qty*price
  print (item, "Quantity is", qty, "Price is $", price, "Extended price is $", extprice)
  totalorders = totalorders + 1
  extpricetotal = extpricetotal + extprice
average = extpricetotal/totalorders

print ("Total number of orders is", totalorders)
print ("The total extended price is $", extpricetotal)
print ("The average order is $", average)

  