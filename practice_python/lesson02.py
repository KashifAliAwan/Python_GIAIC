# # # Operands And Operator
# # floor_division = 16 // 3 # 2
# # print(floor_division)


# # modul_division = 16 % 3 # 0
# # print(modul_division)


# # modul_division = 16 / 3 # 0
# # print(modul_division)


# # # Arithmetic Operators

# # a: int = 10
# # b: int = 3
# # print("a + b  = ", a + b)   #13
# # print("a - b  = ", a - b)   #7
# # print("a * b  = ", a * b)   #30
# # print("a / b  = ", a / b)   #3.3333
# # print("a // b = ", a // b)  #3
# # print("a % b  = ", a % b)   #1
# # print("a % b  = ", a ** b)  #1000


# # # Comparison Operators

# # a: int = 8
# # b: int = 12

# # print("a == b = False ", a == b)  # Equal
# # print("a != b = True ", a != b)  # Not equal
# # print("a > b  = False ", a > b)   # Greater than
# # print("a < b  = True", a < b)   # Less than
# # print("a >= b = False", a >= b)  # Greater than or equal
# # print("a <= b = True", a <= b)  # Less than or equal

# # Hard Example

# # a: int = 10
# # b: int = 5
# # c: int = 20

# # # Complex comparisons with arithmetic operations
# # print("(a + b) * 2 == c = False", (a + b) * 2 == c)          # Check if (10 + 5) * 2 equals 20
# # print("a ** 2 > b * c =   False", a ** 2 > b * c)              # Check if 10^2 is greater than 5 * 20
# # print("(c % a) + b != a = True", (c % a) + b != a)          # Check if (20 % 10) + 5 is not equal to 10
# # print("(a // b) * c <= a + b + c =  False", (a // b) * c <= a + b + c)  # Check if (10 // 5) * 20 <= 10 + 5 + 20 <><> 40
# # print("a * (b + c) >= c ** 2  False= ", a * (b + c) >= c ** 2) # Check if 10 * (5 + 20) >= 20^2
# # print("(a + c) // b == a = False", (a + c) // b == a)        # Check if (10 + 20) // 5 equals 10


# # # Example 1
# # a: bool = True
# # b: bool = True
# # print("a and b = True", a and b)
# # print("a or b  = True", a or b)
# # print("not a   = False", not a)
# # print("Example No 01 <<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>")

# # # Example 2
# # c: bool = False
# # d: bool = False
# # print("c and d = False", c and d)
# # print("c or d  = False", c or d)
# # print("not c   = True", not c)

# # # Example 3
# # e: bool = True
# # f: bool = False
# # print("e and f = False", e and f)
# # print("e or f  = True", e or f)
# # print("not e   = False", not e)

# # # Example 4
# # g: bool = False
# # h: bool = True
# # print("g and h = False", g and h)
# # print("g or h  = True", g or h)
# # print("not g   = True", not g)

# # # Example 5
# # i: bool = True
# # j: bool = True
# # print("i and j = T", i and j)
# # print("i or j  = T", i or j)
# # print("not i   = F", not i)

# # # Example 6
# # k: bool = False
# # l: bool = True
# # print("k and l = F", k and l)
# # print("k or l  = T", k or l)
# # print("not k   = T", not k)

# # # Example 7
# # m: bool = True
# # n: bool = False
# # print("m and n = F", m and n)
# # print("m or n  = T", m or n)
# # print("not m   = F", not m)

# # # Example 8
# # o: bool = False
# # p: bool = False
# # print("o and p = F", o and p)
# # print("o or p  = F", o or p)
# # print("not o   = T", not o)

# # # Example 9
# # q: bool = True
# # r: bool = True
# # print("q and r = T", q and r)
# # print("q or r  = T", q or r)
# # print("not q   = F", not q)

# # # Example 10
# # s: bool = False
# # t: bool = True
# # print("s and t = F", s and t)
# # print("s or t  = T", s or t)
# # print("not s   = T", not s)


# # # Hard Examples

# # # Example 1
# # a = 10
# # b = 5
# # c = 2
# # print("False",(a + b * c > 20) and (a % b == 0) or (c ** 2 != 4))

# # # Example 2
# # x = 7
# # y = 3
# # z = 4
# # print("False",(x // y + z * 2 <= 10) and not (x % y == 1))

# # # Example 3
# # p = 15
# # q = 4
# # r = 3
# # print("True",(p / q + r ** 2 >= 10) or (q % r == 0) and (p - q * r != 3))

# # # Example 4
# # m = 20
# # n = 6
# # o = 2
# # print(not (m // n == 3) and (m % n + o ** 2 > 10) or (n * o < m))

# # # Example 5
# # d = 8
# # e = 3
# # f = 2
# # print((d ** e % f == 0) and (d // e + f != 5) or not (e * f > d))

# # # Example 6
# # g = 25
# # h = 5
# # i = 3
# # print((g / h - i ** 2 == 0) or (h % i == 0) and not (g // h < i))

# # # Example 7
# # j = 12
# # k = 4
# # l = 2
# # print((j % k + l ** 3 > 10) and (j // k - l == 1) or not (k * l < j))

# # Example 8
# # s = 30
# # t = 7
# # u = 3
# # print((s // t + u ** 2 <= 10) or (t % u == 1) and not (s - t * u > 10))
# #       False                     False                   True
# # # Example 9
# # v = 16
# # w = 4
# # x = 2
# # print(True,(v ** x % w == 0) and (v // w + x != 6) or not (w * x > v))
# # #         False                False                  True

# # # Example 10
# # y = 18
# # z = 5
# # a1 = 3
# # print("True",(y / z - a1 ** 2 < 0) or (z % a1 == 0) and not (y // z > a1))
# # #          False                         True                 True


# # Assignment Operator

# # # Example 1
# # x = 10
# # x += 5
# # print("x += 5 → x = 15 ", x)

# # # Example 2
# # y = 20
# # y -= 3
# # print("y -= 3 → y = -17", y)

# # # Example 3
# # z = 7
# # z *= 4
# # print("z *= 4 → z =28", z)

# # # Example 4
# # a = 15
# # a /= 3
# # print("a /= 3 → a =5.0", a)

# # # Example 5
# # b = 25
# # b //= 4
# # print("b //= 4 → b =6", b)


# # Hard Examples

# # Example 1
# x = 10
# x += 5 * 2  # Equivalent to x = x + (5 * 2)
# print("x += 5 * 2 → x = 20 ", x)

# # Example 2
# y = 20
# y -= 3**2  # Equivalent to y = y - (3 ** 2)
# print(f"y -= 3 ** 2 → y = 11 > {y} ")

# # Example 3
# z = 7
# z *= 4 + 2  # Equivalent to z = z * (4 + 2)
# print(f"z *= 4 + 2 → z = 42 > {z}")

# # Example 4
# a = 15
# a /= 3 % 2  # Equivalent to a = a / (3 % 2)
# print("a /= 3 % 2 → a =15", a)

# # Example 5
# b = 25
# b //= 4 + 1  # Equivalent to b = b // (4 + 1)
# print("b //= 4 + 1 → b =5", b)



# # Example 1
# x = [1, 2, 3]
# y = [1, 2, 3]
# z = x
# print("x is z     = True ", x is z)
# print("x is y     = False  ", x is y)
# print("x == y     = True ", x == y)
# print("x is not y = True ", x is not y)
# print("----------")

# # Example 2
# a = [10, 20, 30]
# b = a
# c = [10, 20, 30]
# print("a is b     = True ", a is b)
# print("a is c     = False ", a is c)
# print("a == c     = True ", a == c)
# print("a is not c = True ", a is not c)
# print("----------")
# # Example 3
# p = [5, 6, 7]
# q = [5, 6, 7]
# r = p.copy()
# print("p is q     = Flase ", p is q)
# print("p is r     = False", p is r)
# print("p == q     = True ", p == q)
# print("p is not r = True ", p is not r)
# print("----------")
# # Example 4
# m = [100, 200]
# n = m
# o = [100, 200]
# print("m is n     = True ", m is n)
# print("m is o     = False ", m is o)
# print("m == o     = True ", m == o)
# print("m is not o = True ", m is not o)
# print("----------")
# # Example 5
# d = [1, 2, 3]
# e = d[:]  # Creates a shallow copy
# f = [1, 2, 3]
# print("d is e     = False ", d is e)
# print("d is f     = False ", d is f)
# print("d == f     = True ", d == f)
# print("d is not f = True ", d is not f)

# print('\n-----\n')

# x = [1, 2, 3]
# y = [1, 2, 3]
# z = x
# print(id(z),"Assigning value")
# print(id(x),"Orignal")

# print('\n-----\n')

# d = [1, 2, 3]
# e = d[:]  # Creates a shallow copy
# f = [1, 2, 3]
# print(id(d),"Orignal")
# print(id(e),"Shallow Copy")

# # Example 1: List of numbers
# numbers: list = [10, 20, 30, 40, 50]

# print("numbers           = [10, 20, 30, 40, 50]", numbers)
# print("20 in numbers     = T", 20 in numbers)
# print("100 not in numbers = T", 100 not in numbers)

# print("\n-----\n")

# # Example 2: List of fruits
# fruits: list = ["apple", "banana", "cherry", "date"]

# print("fruits           = ", fruits)
# print("'banana' in fruits = T", 'banana' in fruits)
# print("'grape' not in fruits = T", 'grape' not in fruits)

# print("\n-----\n")

# # Example 3: String with a phrase
# phrase: str = "Python Programming"

# print("phrase           = /", phrase)
# print("'Python' in phrase = T", 'Python' in phrase)
# print("'Java' not in phrase = T", 'Java' not in phrase)

# print("\n-----\n")

# # Example 4: List of mixed types
# mixed_list: list = [1, "hello", 3.14, True]

# print("mixed_list       = ", mixed_list)
# print("'hello' in mixed_list = T", 'hello' in mixed_list)
# print("False not in mixed_list = T", False not in mixed_list)

# print("\n-----\n")

# # Example 5: String with a sentence
# sentence: str = "The quick brown fox jumps over the lazy dog"

# print("sentence         = ", sentence)
# print("'fox' in sentence = T", 'fox' in sentence)
# print("'cat' not in sentence = t", 'cat' not in sentence)



# Example 1: Mixed list with nested lists and strings
# mixed_data: list = [1, "hello", [5, 6, 7], "world", False]

# print("mixed_data       = ", mixed_data)
# print("'hello' in mixed_data = True", 'hello' in mixed_data)
# print("[5, 6, 7] not in mixed_data = False", [5, 6, 7] not in mixed_data)
# print("'world' in mixed_data[2] = False ", 'Kashif Ali' in mixed_data[2])

# print("\n-----\n")

# # Example 2: Complex string with substring checks
# complex_string: str = "The quick brown fox jumps over the lazy dog"

# print("complex_string   = ", complex_string)
# print("'quick' in complex_string = True ", 'quick' in complex_string)
# print("'fox' not in complex_string = False ", 'fox' not in complex_string)
# print("'cat' in complex_string[10:20] = False ", 'cat' in complex_string[10:20])


# slicing_valu:list=["Kashif Ali",2,"Awan",False]
# print(slicing_valu[2][0:2])


# Example 1: Tuple (Immutable and Nested)
# Nested tuple with mixed data types
# nested_tuple: tuple = (1, "apple", (3.14, [5, 6]), {"key": "value"}, True)

# print("nested_tuple      = ", nested_tuple)
# print("'apple' in nested_tuple = True", 'apple' in nested_tuple)
# print("(3.14, [5, 6]) not in nested_tuple = Flse", (3.14, [5, 6]) not in nested_tuple)
# print("'key' in nested_tuple[3] = True", 'key' in nested_tuple[3])

# # Example 2: Set (Unique and Unordered)
# # Set with mixed data types and nested structures
# mixed_set: set = {1, "hello", (2, 3), frozenset({4, 5})}

# print("mixed_set         = ", mixed_set)
# print("(2, 3) in mixed_set = True", (2, 3) in mixed_set)
# print("frozenset({4, 5}) not in mixed_set = False", frozenset({4, 5}) not in mixed_set)
# print("'world' in mixed_set = False ", 'world' in mixed_set)

# # Example 3: Dictionary (Key-V0alue Pairs)
# # Nested dictionary with mixed data types
# nested_dict: dict = {
#     "name": "Alice",
#     "age": 25,
#     "skills": {"Python", "Java", "SQL"},
#     "address": {"city": "Wonderland", "zip": 12345}
# }

# print("nested_dict       = ", nested_dict)
# print("'age' in nested_dict = True", 'age' in nested_dict)
# print("'Python' in nested_dict['skills'] =True ", 'Python' in nested_dict['skills'])
# print("'city' not in nested_dict['address'] = False", 'city' not in nested_dict['address'])

# name = "Kashif Ali"
# _age = 21
# salary2k25 = 4000
# dictionary :dict = {
#     "Name" : name,
#     "Age" : _age,
#     "Salary" : salary2k25
# }
# dtol= tuple(dictionary.values())
# print(dtol[1:4])
# print(dtol)


# import keyword

# # Line continuation (`\`) allows printing a statement over multiple lines, improving code readability without breaking the string.
# print("The list of keywords is : ")

# # printing all keywords at once using "kwlist()"
# print(keyword.kwlist)