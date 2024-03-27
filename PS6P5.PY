# THIS PROGRAM WILL CALCULATE BONUS RATE BASED ON RANK 
print ("Enter employee name")
name = str(input())
print ("Enter employee salary")
salary = float(input())
print ("Enter employee job level")
rank = int(input())

if rank >10:
  brate = 0.25
else:
  if rank >5 and rank <9:
    brate = .20
  else:
    brate = .10

bonus = salary*brate
print ("Employee name is " + str(name))
print ("Employee bonus is $" + str(bonus))