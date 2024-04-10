#THIS PROGRAM WILL DISPLAY NUMBERS FROM START TO FINISH
start = int(input( "Enter start value:"))
stop = int(input("Enter stop value:"))
increment = int(input("Enter increment value:"))

count = start 
while count <= stop:
  print (count)
  count += increment
