lastname = ["AA", "BB", "CC", "DD", "EE", "FF", "GG", "HH", "II", "JJ"]
def shownames(names):
  for name in names:
    print (name)

def showrnames(names):
  for name in reversed(names):
    print (name)

shownames(lastname)
print ("REVERSED")
showrnames(lastname)