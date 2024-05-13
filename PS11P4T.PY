def loaddata(players, battingavg):
  players_list = []
  battingavg_list = []
  with open("batters.txt", "r") as f:
      for line in f:
          data = line.strip().split(",")
          players_list.append(data[0])
          battingavg_list.append(float(data[1]))
  return players_list, battingavg_list

def display(players, battingavg):
  print("Player Names and Batting Averages")
  for i in range(len(players)):
      print(players[i], "Batting Average:", battingavg[i])

def search(players, battingavg):
  namesearch = input("Would you like to enter a player's name? If yes, type 'Y'")
  while namesearch == 'Y':
      name = input("Enter a player's name: ")
      if name in players:
          index = players.index(name)
          print("The batting average for", name, "is", battingavg[index])
      namesearch = input("Would you like to enter another name? Enter 'Y' if yes: ")

players = []
battingavg = []
players, battingavg = loaddata(players, battingavg)
display(players, battingavg)
search(players, battingavg)