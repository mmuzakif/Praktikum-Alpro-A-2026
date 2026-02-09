#match
month = 5
day = 4
match day:
  case 1 | 2 | 3 | 4 | 5 if month == 4:
    print("A weekday in April")
  case 1 | 2 | 3 | 4 | 5 if month == 5:
    print("A weekday in May")
  case _:
    print("No match"))

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

for x in range(6):
  print(x)

for x in range(2, 6):
  print(x)
