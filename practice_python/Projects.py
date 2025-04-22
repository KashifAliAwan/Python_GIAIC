
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

# unit = input("Enter Unit which You Wants to Convert — Celsius (C) or Fahrenheit (F) ")
# temprature = float(input("Please Enter Number "))


# if unit.lower() == "c":
#     converted = (temprature * 9 / 5) + 32
#     print(f"{temprature}°C  is Equal to {converted}°F")
# elif unit.lower() == "f":
#     converted = (temprature + 32 ) * 5/9
#     print(f"{temprature}°F is Equal to  {converted}°C")
# else:
#     print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")


#   <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>><<<<<<<<<<<<<<<>>>>>>>>>>>
#      <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>><<<<<<<<<<<<<<<>>>>>>>>>>>>><<<>
#          <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>><<<<<<<<<<<<<<<>>>>>>>>>>>>><<<<<<<>>
#             <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>><<<<<<<<<<<<<<<>>>>>>>>>>>>><<<<<<<<<<<<>>
#                <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>><<<<<<<<<<<<<<<>>>>>>>>>>>>><<<<<<<<<<<<>>>>>>>


# 4. Shopping List App
# Let users add items one by one
# Stop when user types "done"
# Show the full list
# Practice: lists, loops, append()


# shop_list = []
# while True:
#     user_input : str = input("Add Items One by One Please ")
#     if user_input.lower() == "done":
#         break
#     shop_list.append(user_input)


# # Step 5: Print all items in the list
# print("\nYour Shopping List:")
# for item in shop_list:
#     print("- " + item)



#   <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>><<<<<<<<<<<<<<<>>>>>>>>>>>
#      <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>><<<<<<<<<<<<<<<>>>>>>>>>>>>><<<>
#          <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>><<<<<<<<<<<<<<<>>>>>>>>>>>>><<<<<<<>>
#             <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>><<<<<<<<<<<<<<<>>>>>>>>>>>>><<<<<<<<<<<<>>
#                <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>><<<<<<<<<<<<<<<>>>>>>>>>>>>><<<<<<<<<<<<>>>>>>>


# Todo App

# ToDo_list = []
# user_name: str = input("Enter Your Name ")
# ask = input(f"Hey {user_name} You Wants to Create Your ToDo List - \n Y or N ")
# if ask.lower() == "y":
#     while True:
#         user_input = input("My ToDo List - ")
#         if user_input.lower() == "done":
#             break

#         ToDo_list.append(user_input)

# # Showing Complete Todo List
#     print("\n Your Complete Todo List Here")
#     for item in ToDo_list:
#         print(f"- {item}")

# elif ask.lower() == "n":
#     print(f":) Okay {user_name} Its Your Choice Bro")



#   <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>><<<<<<<<<<<<<<<>>>>>>>>>>>
#      <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>><<<<<<<<<<<<<<<>>>>>>>>>>>>><<<>
#          <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>><<<<<<<<<<<<<<<>>>>>>>>>>>>><<<<<<<>>
#             <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>><<<<<<<<<<<<<<<>>>>>>>>>>>>><<<<<<<<<<<<>>
#                <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>><<<<<<<<<<<<<<<>>>>>>>>>>>>><<<<<<<<<<<<>>>>>>>




# . Guess the Number
# Let the program randomly pick a number
# User keeps guessing until they get it right
# Practice: loops, comparison, import random



# import random
# # secret_number = random.randint(1,10)
# # print(secret_number)
# while True:
#     secret_number = random.randint(1,20)
#     if secret_number == 2:
#         break
#     print(secret_number)


# <<<<<>>><<<<<<<<<>>>>>>>><<<<>>><<<<>

# import random
# def guessing_number():
#     secret_number = random.randint(1,5)
#     attempts = 0
#     print("Guess Number between 1 to 5")
#     while True:
#         guess = int(input("Guess Number "))
#         attempts += 1

#         if guess > 0 :   
#             if guess == secret_number:
#                 print(f"Correct! You guessed it in {attempts} tries.") 
#                 break 
#             elif guess < secret_number:
#                 print("Too low! Try again. ")
#             else:
#                 print("Too high! Try again. ")
#         else:
#             print("Please Enter Number Greaten than 0")

# guessing_number()


#   <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>><<<<<<<<<<<<<<<>>>>>>>>>>>
#      <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>><<<<<<<<<<<<<<<>>>>>>>>>>>>><<<>
#          <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>><<<<<<<<<<<<<<<>>>>>>>>>>>>><<<<<<<>>
#             <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>><<<<<<<<<<<<<<<>>>>>>>>>>>>><<<<<<<<<<<<>>
#                <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>><<<<<<<<<<<<<<<>>>>>>>>>>>>><<<<<<<<<<<<>>>>>>>



# 7. Age Calculator
# Ask for birth year
# Calculate and print the user's age
# Practice: arithmetic, current year (can use datetime)

# from datetime import datetime
# def age_calculator():
#     user_name = input("Enter Your Name Here : ")
#     user_age = int(input("Enter Your Birth Year : "))
#     current_year = datetime.now().year
#     age : int = (current_year - user_age)
#     print(f"Hey {user_name} Your age is {age}")

# age_calculator()

#   <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>><<<<<<<<<<<<<<<>>>>>>>>>>>
#      <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>><<<<<<<<<<<<<<<>>>>>>>>>>>>><<<>
#          <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>><<<<<<<<<<<<<<<>>>>>>>>>>>>><<<<<<<>>
#             <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>><<<<<<<<<<<<<<<>>>>>>>>>>>>><<<<<<<<<<<<>>
#                <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>><<<<<<<<<<<<<<<>>>>>>>>>>>>><<<<<<<<<<<<>>>>>>>



# 6. Mini Quiz App
# Ask 3–5 multiple choice questions
# Count score
# Give results at the end
# Practice: if-else, input, logical operators

# score = 0
# from colorama import Fore,Style


# print(" Question 1: What is the capital of France? \n A) Rome  B) Berlin C) Paris")
# answer = input("Your Answer : ")
# if answer.lower() == "c":
#     score += 10
#     print(Fore.GREEN + "Correct Answer" + Style.RESET_ALL)
# else:
#     print(Fore.RED + 'Your Answer in Wrong!' + Style.RESET_ALL)


# print("Question 2: What is 5 x 3? \n A) 15 B) 8 C) 10")
# answer = input("Your Answer : ")
# if answer.lower() == "a":
#     score += 10
#     print(Fore.GREEN + "Correct Answer" + Style.RESET_ALL)
# else:
#     print(Fore.RED + 'Your Answer in Wrong!' + Style.RESET_ALL)


# print("Question 3: What color do you get when you mix red and yellow? \n A) Orange B) Purple C) Green")
# answer = input("Your Answer : ")
# if answer.lower() == "a":
#     score += 10
#     print(Fore.GREEN + "Correct Answer" + Style.RESET_ALL)
# else:
#     print(Fore.RED + "Your Answer is Wrong!" + Style.RESET_ALL)

# print("Question 4: How many legs does a spider have? \n A) 6 B) 8 C) 10")
# answer = input("Your Answer : ")
# if answer.lower() == "b":
#     score += 10
#     print(Fore.GREEN + "Correct Answer" + Style.RESET_ALL)
# else:
#     print(Fore.RED + "Your Answer is Wrong!" + Style.RESET_ALL)

# print("Question 5: Which gas do plants use to make food? \n A) Oxygen B) Hydrogen C) Carbon Dioxide")
# answer = input("Your Answer : ")
# if answer.lower() == "c":
#     score += 10
#     print(Fore.GREEN + "Correct Answer" + Style.RESET_ALL)
# else:
#     print(Fore.RED + "Your Answer is Wrong!" + Style.RESET_ALL)

# print(Fore.CYAN + "\n🎉 Quiz Finished! You scored", score, "out of 50." + Style.RESET_ALL )







# questions = [
#     ["What is the capital of France? A) Paris B) Rome C) Berlin", "a"],
#     ["What is 2 + 2? A) 3 B) 4 C) 5", "b"],
#     ["Which planet is known as the Red Planet? A) Earth B) Mars C) Venus", "b"]
# ]

# score = 0
# i = 0

# while i < len(questions):
#     print(questions[i][0])
#     answer = input("Your answer: ")
#     if answer.lower() == questions[i][1]:
#         score += 1
#     i += 1

# print("You got", score, "out of", len(questions))
