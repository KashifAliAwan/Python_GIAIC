# # Operands And Operator
# floor_division = 16 // 3 # 2
# print(floor_division)


# modul_division = 16 % 3 # 0
# print(modul_division)


# modul_division = 16 / 3 # 0
# print(modul_division)



# # Arithmetic Operators

# a: int = 10
# b: int = 3
# print("a + b  = ", a + b)   #13
# print("a - b  = ", a - b)   #7
# print("a * b  = ", a * b)   #30
# print("a / b  = ", a / b)   #3.3333
# print("a // b = ", a // b)  #3
# print("a % b  = ", a % b)   #1
# print("a % b  = ", a ** b)  #1000


# # Comparison Operators

# a: int = 8
# b: int = 12

# print("a == b = False ", a == b)  # Equal
# print("a != b = True ", a != b)  # Not equal
# print("a > b  = False ", a > b)   # Greater than
# print("a < b  = True", a < b)   # Less than
# print("a >= b = False", a >= b)  # Greater than or equal
# print("a <= b = True", a <= b)  # Less than or equal

#Hard Example

a: int = 10
b: int = 5
c: int = 20

# Complex comparisons with arithmetic operations
print("(a + b) * 2 == c = False", (a + b) * 2 == c)          # Check if (10 + 5) * 2 equals 20
print("a ** 2 > b * c =   False", a ** 2 > b * c)              # Check if 10^2 is greater than 5 * 20
print("(c % a) + b != a = True", (c % a) + b != a)          # Check if (20 % 10) + 5 is not equal to 10
print("(a // b) * c <= a + b + c =  False", (a // b) * c <= a + b + c)  # Check if (10 // 5) * 20 <= 10 + 5 + 20 <><> 40
print("a * (b + c) >= c ** 2  False= ", a * (b + c) >= c ** 2) # Check if 10 * (5 + 20) >= 20^2
print("(a + c) // b == a = False", (a + c) // b == a)        # Check if (10 + 20) // 5 equals 10