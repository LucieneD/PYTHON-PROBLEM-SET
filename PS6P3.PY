#THIS PROGRAM WILL COMPUTE FIRST YEAR INTREST OF A CD BASED ON PRINCIPAL AND MATURITY
print ("Enter the principal")
principal = float(input())
print ("Enter the maturity")
maturity = int(input())
if principal > 100000 and maturity == 5:
  intrest = 0.06
  if principal >= 50000 and maturity == 10:
    intrest = 0.05
    if principal >= 50000 and maturity == 5:
      intrest = 0.04
else: intrest = 0.02
fyg = principal*intrest
print ("The first year interest is " + str(fyg))