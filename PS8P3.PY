f = open("PS8P3.txt", "r")
name = f.readline().rstrip('\n')
totalbonus = 0
while name != "":
  salary = float(f.readline().rstrip('\n'))
  if salary >= 100000:
    bonusrate = 0.20
    if salary == 50000:
      bonusrate = 0.15
  else:
    bonusrate = 0.10
  bonus = salary*bonusrate
  print (name, "Salary is", str(salary), "Bonus is", str(bonus))
  totalbonus = totalbonus + bonus
  name = f.readline()
print ("The total bonus is", totalbonus)
