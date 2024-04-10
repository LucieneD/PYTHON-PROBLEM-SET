#THIS PROGRAM WWILL DISPLAY ODD NUMBERS FROM 1-25
start = 1
stop = 25
while start <= stop:
  odd = start % 2
  if odd != 0:
    print (start)
  start = start +1

  