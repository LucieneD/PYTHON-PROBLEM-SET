#THIS PROGRAM WILL CALCULATE MEAL TIP AT 15%, 18% AND 20%
print ("Enter the total price of your meal")
meal = input()
tip15 = float(meal)*0.15
tip18 = float(meal)*0.18
tip20 = float(meal)*0.20
print ("If you would like to tip 15%,", "\n the tip is", tip15, "\n", "the total price is$", float(meal)+tip15)
print ("If you would like to tip 18%," , "\n The tip is",tip18, "\n", "The total price is$", float(meal)+tip18)
print ("If you would like to tip 20%," , "\n The tip is", tip20, "\n", "The total price is$",float(meal)+tip20)