#THIS PROGRAM WILL CALCULATE THE COST OF CONCERT TICKETS BASED ON VOLUME OF TICKETS
print ("Enter number of tickets")
tickets = int(input())
if tickets >= 25:
  price = 50
else:
  if tickets >10 and tickets <24:
    price = 60
  else:
    if tickets >5 and tickets <9:
      price = 70
    else:
      price = 75

total = tickets*price
print ("You are purchasing " + str(tickets) + "tickets to the concert")
print ("The price per ticket is $ " + str(price))
print ("The total cost is $" + str(total))