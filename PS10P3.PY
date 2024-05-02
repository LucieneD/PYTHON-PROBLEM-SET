#create function to calculate discounted price
def discount(qty, price, disrate):
  total = price *qty
  disamt = price*disrate
  disprice = total - disamt
  return disamt, disprice

qty = float(input("Enter qty you wish to purchase"))
price = float(input("Enter price per item"))
disrate = float(input("Enter discount rate"))
amtoff, newprice  = discount(qty, price, disrate)
print ("The discount amount is $", amtoff)
print ("The new price is $", str(newprice))

