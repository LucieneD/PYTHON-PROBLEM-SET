#This program will compute the warranty of an appliance
print ("Enter the name of the appliance")
appliance = input()
print ("Enter the cost of the appliance")
cost = float(input())

if cost > 1000:
  warranty = cost*.10
else:
  warranty = .05

total = cost + warranty
print ("The name of the appliance is " + appliance)
print ("The cost of warranty for this appliance is " + str(warranty))
print ("The total cost of this appliance is " + str(total))
