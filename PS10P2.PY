from func import sqft

while True:
  response = input ("Do you want to calculate the square footage of a room? If yes, enter 'Y'")
  if response == "Y":
    length = float(input("Enter the length of the room"))
    width = float(input("Enter the width of the room"))
    height = float(input("Enter the height of the room"))
    roomsqft = sqft(length, width, height)
    gallonsneed = roomsqft/50
    print ("The square footage of the room is", roomsqft)
    print ("The number of gallons needed is", gallonsneed)