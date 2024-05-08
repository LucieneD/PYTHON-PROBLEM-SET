
def loaddata(name,score):
  data = []
  with open ("namescore.txt", "r") as file:
    for line in file:
      name, score = line.strip().split()
      data.append((name, int(score)))
    return data

def findhighest(data):
  highest = 0
  lowest = 999
  highname = ""
  lowname = ""
  for name, score in data:
    if score > highest:
      highest = score
      highname = name
    if score < lowest:
      lowest = score
      lowname = name
  return highest, highname, lowest, lowname 

def display(highname, lowname):
  print ("The name with the highest score is: ", highname)
  print ("The name with the lowest score is: ", lowname)

#main
name = ""
score = ""
data = loaddata(name,score)
highname,highest, lowname,lowest = findhighest(data)
print (highname, highest, lowname, lowest,)
  