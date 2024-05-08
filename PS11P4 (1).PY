players = []
battingavg = 0
with open ("batters.txt", "r") as f:
  players= f.readline().rstrip('\n')
  battingavg = f.readline().rstrip('\n')

loop = input("Would you like to enter a players name? If yes type 'Y'")
while loop == 'Y':
  name = (input("Enter a players name"))
  if name in players:
    index = players.index(name)
    print ("The batting average is", battingavg[index])
  else:
    print ("The player is not in the list")

  loop = input("Would you like to enter another players name? If yes type 'Y'")
  