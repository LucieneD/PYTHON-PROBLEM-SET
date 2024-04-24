def calcmpg(miles, gallons):
  mpg= miles/gallons
  return mpg

loop = input("Would you like to enter a city? If yes, enter Y")
trips = 0
while loop == "Y":
  city = input("Enter a city you wish to travel to ")
  miles = int(input("Enter miles traveled"))
  gallons = int(input("Enter gallons used"))
  mpg = calcmpg(miles, gallons)
  trips = trips+1
  print (city, "Miles entered ", miles, "Miles per gallon is ", mpg)
  loop = input("Would you like to enter another city? If yes, enter 'Y'")

print ("The total number of trips is", trips)