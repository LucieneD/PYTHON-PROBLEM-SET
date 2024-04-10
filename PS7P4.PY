#COMPUTE GROSS PAY, TOTAL PAY AND AVERAGE PAY OF EMPLOYEES
totalpays = 0
totalemployees = 0
grosspay = 0
while True:
  response = str(input ("Do you want to continue? Enter 'yes' to continue"))
  if response != 'yes':
    break
  name= input ("Enter your last name")
  hours = float(input("How many hours have you worked"))
  rate = float(input("What is your hourly rate"))
  if hours > 40:
     grosspay = grosspay + (hours - 40) * rate * 0.5 
  else:
      grosspay = hours * rate
  print ("Hello" + name + "Your gross pay is" + str(grosspay))
  totalpays = totalpays + grosspay
  totalemployees = totalemployees + 1
  response2 = str(input("Would you like to enter another employee? Enter 'yes' to continue"))
  if response2 != 'yes':
    break
    
if totalemployees > 0:
    averagepay = totalpays/ totalemployees
    print ("The total number of employees entered: " + str(totalemployees))
    print ("The total pay of all employees is: " + str(totalpays))
    print ("The average pay of all employees is: " + str(averagepay))
