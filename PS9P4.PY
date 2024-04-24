#get pay rate based on jobcode
def getpayrate(jobcode,rate):
  grosspay=0
  if jobcode == "L":
    rate = 25.00 
  elif jobcode == "A":
    rate = 30.00
  elif jobcode == "J":
    rate = 50.00
  return rate
    
def calcgrosspay (hours,rate):
  
  if hours > 40:
    reghours =40
    othours = hours - 40
    return reghours*rate + othours*rate*1.5
  else:
    return hours*rate
  return grosspay 

#initialize variables
sumpay = 0
loop = input ("Do you want to calculate pay? If yes, enter 'Y'")
while loop == 'Y':
  name = str(input("Enter last name"))
  hours = float (input(" Enter hours worked :"))
  jobcode = input(" Enter job code: ")
  rate = 0
  rate = getpayrate(jobcode,rate)
  grosspay = calcgrosspay (hours,rate)
  print (name, "Your gross pay is $ ", grosspay)
  sumpay = sumpay + grosspay
  loop = input("Do you want to calculate another pay? If yes, enter 'Y'")

print ("The sum of all gross pay is $", sumpay)