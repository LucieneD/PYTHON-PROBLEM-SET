from func import salesforecast

loop = str(input("Would you like to enter a month? If yes, enter YES "))
while loop == "YES":
  name = str(input("Enter last name"))
  month = str(input("Enter a month"))
  sales = float(input("Enter sales"))
  forecast = salesforecast(month,sales)
  print ("Hello", name, "Your forcast sales is", forecast)
  loop = str(input("Would you like to enter another month? If yes, enter 'YES'"))

