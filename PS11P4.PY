f = open ("batters.txt", "r")
players = ""
battingavg = 0
players= f.readline().rstrip('\n')
battingavg = f.readline().rstrip('\n')

loop = ("Would you like to enter a players name? If yes type 'Y'")
while loop == 'Y':
  name = str(input("Enter a players name"))
  if name in players:
    index = players.index(name)
    print ("The batting average is", battingavg[index])
  else:
    print ("The player is not in the list")