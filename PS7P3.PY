#THIS PROGRAM WILL ONLY CONTINUE IF THE USER ANSWERS YES
studentcount = 0
while True:
  response = input("Do you want to continue? Enter 'Yes' to continue")
  if response != 'yes':
    break
  else:
    name = input ("Enter your last name")
    exam1 = float(input("Enter exam 1 score"))
    exam2 = float(input("Enter exam 2 score"))
    average = (exam1 + exam2) / 2
  print ("Hello" + name + " Your average exam score is " + str(average))
  studentcount = studentcount + 1
  response2 = input("Do you want to enter another student? Enter 'Yes' to continue")
  if response2 != 'yes':
    break

print ("Total number of students:" + str(studentcount))