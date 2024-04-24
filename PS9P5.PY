#get cost of tuition based on district code
def getcode(code,cost):
  if code == 'I':
    cost = 250.00
  elif code == 'O':
    cost = 550.00
  return cost

#calculate cost of tuition based on credits and code
def calctuition(hours,cost):
  tuition = hours*cost
  return tuition

#initialize variables
sumpay = 0
loop = input("Do you want to calculate tuition? If yes, enter 'Y'")
while loop == 'Y':
  name = str(input("Enter last name of student "))
  hours = float(input("Enter credit hours "))
  code = input("Enter district code: ")
  cost = 0
  cost = getcode (code,cost)
  tuition = calctuition(hours, cost)
  print ("Hello ", name, "!", "Your total cost of tuition is $", tuition)
  sumpay = sumpay + tuition
  loop = input ("Would you like to calulate tuition for another student? If yes, Enter 'Y'")

print ("The sum of all tuitions calculated is $", sumpay)