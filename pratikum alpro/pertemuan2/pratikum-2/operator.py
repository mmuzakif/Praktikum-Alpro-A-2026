print("hi")
sum1 = 100 + 50      # 150 (100 + 50)
sum2 = sum1 + 250    # 400 (150 + 250)
sum3 = sum2 + sum2   # 800 (400 + 400)
#modulus
print(15 // 2)
x = 15
y = 2
#math operator
print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x % y)
print(x ** y)
print(x // y)
 #assignment
numbers = [1, 2, 3, 4, 5]
if (count := len(numbers)) > 3:
    print(f"List has {count} elements")

#comparison 
x = 5
y = 3
print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)
# and,or
x = 5
print(x > 0 and x < 10)
x = 5
print(x < 5 or x > 10)
x = 5
print(not(x > 3 and x < 10))
#identity
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
print(x is z)
print(x is y)
print(x == y)
x = ["apple", "banana"]
y = ["apple", "banana"]
print(x is not y)
#
fruits = ["apple", "banana", "cherry"]

print("banana" in fruits)
# bitwise
print(6 & 3)
print(6 | 3)
print(6 ^ 3)
#precedence
print((6 + 3) - (6 + 3))
print(100 + 5 * 3)
#
