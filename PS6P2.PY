#THIS PROGRAM WILL DETERMINE COST PER UNIT BASED ON PART NUMBER
print ("Enter the part number")
part = str(input())
print ("enter the quantity you wish to purchase")
qty = float(input())
if part == "10" or part == "55":
  uprice = 1.00
  if part == "99":
    uprice = 2.00
    if part == "80" or part == "70":
      uprice = 3.00
        
else: uprice = 5.00

total = (qty*uprice)
print ("for part number" + str(part))
print ("The unit price is $ " + str(uprice))
print ("The total price is $ " + str(total))