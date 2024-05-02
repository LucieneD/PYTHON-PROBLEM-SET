total = 0
tax =0
def calcsubtotal(qty, price):
  global total, tax
  total = qty * price
  tax = total * 0.07

qty = float(input("Enter quantity of the item: "))
price = float(input("Enter price of the item: "))


calcsubtotal(qty,price)
print("Subtotal: $", total)
print ("The Tax is $", tax)