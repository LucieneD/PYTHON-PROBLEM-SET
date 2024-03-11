#THIS PROGRAM WILL CALCULATE HOW MANY CALORIES BURNED ACCORDING TO THE AMOUNT OF STEPS THE USER TAKES PER DAY 
print ("Enter your first name")
name = str(input())
print ("Enter the number of steps you walked today")
steps = int(input())
Calories = steps * 0.25
print ("Hi There," + name)
print ("Your burned", Calories, "calories today")