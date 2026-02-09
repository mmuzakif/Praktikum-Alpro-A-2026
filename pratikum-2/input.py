number = 15
if number > 0:
  print("The number is positive")

a = 33
b = 200
if b > a:
  print("b is greater than a")
# shorthand if
a = 5
b = 2
if a > b: print("a is greater than b")
a = 2
b = 330
print("A") if a > b else print("B")
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")
#nested if
score = 92
extra_credit = 5

if score >= 90:
  if extra_credit > 0:
    print("A+ grade")
  else:
    print("A grade")
elif score >= 80:
  print("B grade")
else:
  print("C grade or below")