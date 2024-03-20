#This program will compute the income tax based on number of dependents and gross income
print ("Enter your last name")
lastname = input()
print ("Enter your gross income")
grossincome = float(input())
print ("Enter number of dependents")
dependents = int(input())
adjgross = grossincome - (dependents*12000)
taxrate=0
if adjgross > 50000:
  taxrate = 0.2
if adjgross < 50000:
  taxrate = 0.1

incomet = adjgross*taxrate

if incomet < 0:
  incomet = 100

print (lastname)
print ("Your gross income is $" + str(grossincome))
print ("Your number of dependents is " + str(dependents))
print ("Your adjusted gross income is $" + str(adjgross))
print ("Your income tax is $" + str(incomet))
