loop = (input("Y if you would like to loop"))
totalinterest = 0
while loop == "Y":
  principal = float(input("Enter principal amount"))
  rate = float(input("Enter intrest rate in decimal form"))
  totalinterest = 0
  print ("\n Year", "Beg Balance", "End Balance")
  for y in range (1,6,1):
    interest = principal*rate
    endingbalance = principal+interest
    print ("\n Year", "{:.2F}" .format(principal), "{:.2F}" .format(endingbalance))
   
    totalinterest = totalinterest + interest
print("\n Total interest earned is $", "{:.2F}".format(totalinterest))
loop = (input("Y if you would like to loop"))
