#
discountamt = 0
while True:
  response = input("Do you want to continue? Enter 'Yes' to continue")
  if response != 'yes':
    break
  else:
    qty = int(input("Enter a quantity"))
    price = float(input("Enter the price of an item"))
    extprice = qty * price
    if extprice > 10000.00:
      discount = 0.25
    else:
      discount = 0.10
    discountamt = extprice * discount
    total = extprice - discountamt
    print ("Extended price: " + str(extprice))
    print ( "Discount amount: " + str(discountamt))
    print ("Total: " + str(total))
    response2 = input("Do you want to enter another item? Enter 'Yes' to continue")
    if response2 != 'yes':
      break
sum = discountamt + discountamt
print ("Sum of all discounts: " + str(sum))