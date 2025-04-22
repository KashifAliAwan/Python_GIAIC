#### Calculator By Kashif Ali

# num1 : int = int(input("Please Enter First Digit "))
# operator : str = input("Please Enter an Operator ")
# num2 : int = int(input("Please Enter Second Digit "))

# if operator == "+":
#  print(num1 + num2)
# elif operator == "-":
#  print(num1 - num2)
# elif operator == "*":
#  print(num1 * num2)
# elif operator in ["/", "//"] and num2 == 0:
#     print("Error: Cannot divide by zero.")
# elif operator == "/":
#  print(num1 / num2)
# elif operator == "//":
#  print(num1 // num2)
# else:
#  print("Please Select Corect Operator")

#   <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>><<<<<<<<<<<<<<<>>>>>>>>>>>
#      <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>><<<<<<<<<<<<<<<>>>>>>>>>>>>><<<>
#          <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>><<<<<<<<<<<<<<<>>>>>>>>>>>>><<<<<<<>>
#             <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>><<<<<<<<<<<<<<<>>>>>>>>>>>>><<<<<<<<<<<<>>
#                <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>><<<<<<<<<<<<<<<>>>>>>>>>>>>><<<<<<<<<<<<>>>>>>>
#                   <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>><<<<<<<<<<<<<<<>>>>>>>>>>>>><<<<<<<<<<<<>>>>>>>>>>>>>
#                      <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>><<<<<<<<<<<<<<<>>>>>>>>>>>>><<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>
#                        <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>><<<<<<<<<<<<<<<>>>>>>>>>>>>><<<<<<<<<<<<>>>>>>>>>>><<<<>>>>>>>>>>
#                          <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>><<<<<<<<<<<<<<<>>>>>>>>>>>>><<<<<<<<<<<<>>>>>>>>>>><<<<>>>>>>>>>>>>>>>>>


# 2. Even or Odd Checker
# Ask the user for a number
# Print whether it's even or odd
# Practice: %, if, int(), input/output

# user_name : str = str(input("Please Enter Your Name "))
# user_input : int = int(input(" Please Enter a Number "))

# if user_input > 0:
#     if user_input % 2 == 0 :
#         print(f"Hey {user_name} You Typed {user_input}  Which is an Even Number")
#     else :
#         print(f"Hey {user_name} You Typed {user_input}  Which is an Odd Number")
# else:
#     print(f"Hey {user_name} Please Type Number Greater than 0")


#   <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>><<<<<<<<<<<<<<<>>>>>>>>>>>
#      <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>><<<<<<<<<<<<<<<>>>>>>>>>>>>><<<>
#          <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>><<<<<<<<<<<<<<<>>>>>>>>>>>>><<<<<<<>>
#             <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>><<<<<<<<<<<<<<<>>>>>>>>>>>>><<<<<<<<<<<<>>
#                <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>><<<<<<<<<<<<<<<>>>>>>>>>>>>><<<<<<<<<<<<>>>>>>>
#                   <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>><<<<<<<<<<<<<<<>>>>>>>>>>>>><<<<<<<<<<<<>>>>>>>>>>>>>
#                      <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>><<<<<<<<<<<<<<<>>>>>>>>>>>>><<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>
#                        <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>><<<<<<<<<<<<<<<>>>>>>>>>>>>><<<<<<<<<<<<>>>>>>>>>>><<<<>>>>>>>>>>
#                          <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>><<<<<<<<<<<<<<<>>>>>>>>>>>>><<<<<<<<<<<<>>>>>>>>>>><<<<>>>>>>>>>>>>>>>>>


# 3. Temperature Converter
# Convert Celsius to Fahrenheit and vice versa
# Practice: math formulas, user input, data types

unit = input("Enter Unit which You Wants to Convert — Celsius (C) or Fahrenheit (F) ")
temprature = float(input("Please Enter Number "))


if unit.lower() == "c":
    converted = (temprature * 9 / 5) + 32
    print(f"{temprature}°C  is Equal to {converted}°F")
elif unit.lower() == "f":
    converted = (temprature + 32 ) * 5/9
    print(f"{temprature}°F is Equal to  {converted}°C")
else:
    print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")    
