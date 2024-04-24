def calcbattingaverage (hits, atbats):
  battingaverage = hits/atbats
  return battingaverage

players = 9
for _ in range (1,players+1):
  lastname = input("Enter last name")
  hits = int(input("Enter number of hits"))
  atbats = int(input("Enter number of atbats"))
  battingaverage = calcbattingaverage(hits, atbats)
  print ("Hello", lastname, "Your batting average is", battingaverage)
  players = players
print ("The total number of players is", players)
