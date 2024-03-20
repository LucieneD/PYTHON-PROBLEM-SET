#This program will calculate total cost + shipping for books
print ("Enter the number of books")
books = int(input())
print ("Enter cost of books")
cost = float(input())

total = cost*books

if total >= 50.00:
  shipping = 0.00
else:
  shipping = 25.00

ordertotal = total+shipping

print ("Your order total" + str(ordertotal))
print ("Your shipping cost is" + str(shipping))