# THIS PROGRAM WILL READ STUDENT NAME, DISTRICT CODE AND NUMBER OF CREDITS AND COMPUTE TUITION 
# open a text file with students name, district code and number of credits
f = open("PS8P5.txt", "r")
name = f.readline().rstrip('/n')
totaltution = 0
count = 0

#loop until the last name reads
while name != "":
  dcode = str(f.readline().rstrip('/n'))
  if dcode == "I":
    costpercredit = 250.00
  else:
    costpercredit = 500.00
  credits = int(f.readline())
  tution = credits*costpercredit
  print (name, "Credits taken are", credits, "Tution is $", tution)
  count = count +1
  totaltution = totaltution + tution
  name = f.readline().rstrip('/n')

print("The total tuition is $", totaltution, "The total number of students is", count)