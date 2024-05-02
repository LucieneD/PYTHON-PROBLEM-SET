def calcscore(score):
  total= sum(score)
  average = total/len(score)
  return total, average


average = 0
lastname = str(input("Enter students last name: "))
exam1 = float(input("Enter exam 1 score: "))
exam2 = float(input("Enter exam 2 score: "))
exam3 = float(input("Enter exam 3 score: "))
score = [exam1, exam2, exam3]
total, average = calcscore(score)

print ("Hello ", lastname, "!")
print ("Your exam score average is ", average)

