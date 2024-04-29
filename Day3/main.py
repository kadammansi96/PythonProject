# # # Write a program for ticketing system for roller coaster ride.
print("Welcome to roller coaster ride")
height = int(input("What is your height in cm?"))
if height >= 120:
  print("You can ridethe roller coaster!")
else:
  print("Sorry, you have to grow taller before you can ride")

# # Write a program to check whether a number is even or odd.

number = int(input("Which number do you want to check?"))
if number % 2 == 0:
  print("This is an even number")
else:
  print("This is an odd number")

# # Write a program for ticketing system for roller coaster ride using nested if else statement.

print("Welcome to roller coaster ride")
height = int(input("What is your height in cm?"))
age = int(input("What is your age?"))
if height >= 120:
  if age < 12:
    print("You can ride the roller coaster and you have to pay $5")
  elif age < 18:
    print("You can ride the roller coaster and you have to pay $7")
  else:
    print("You can ride the roller coaste and you have to pay $12")
else:
    print("Sorry, you have to grow taller before you can ride")

# # Write a program to interpret the Body Mass Index (BMI) based on a user's weight and height.

height = float(input("What is your height in m?"))
weight = float(input("What is your weight in kg?"))
bmi = round(weight / height ** 2)
print(f"bmi is {bmi}")
if bmi < 18.5:
  print("They are underweight")
elif bmi < 25:
  print("They have a normal weight")
elif bmi < 30:
  print("They are overweight")
elif bmi < 35:
  print("They are obese")
else:
  print("They are clinically obese")

# # Write a program to check whether a year is a leap year or not.

year = int(input("Which year do you want to check?"))
if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        print("Leap year")
      else:
        print("Not leap year")
    else:
      print("Leap year")
else:
  print("Not leap year")

# # # Write a program for roller coaster ride with photo.

print("Welcome to roller coaster ride")
height = int(input("What is your height in cm?"))
age = int(input("What is your age?"))
bill = 0
if height >= 120:
  if age < 12:
    bill = 5
    print("You can ride the roller coaster and you have to pay $5")
  elif age < 18:
    bill = 7
    print("You can ride the roller coaster and you have to pay $7")
  else:
    bill = 12
    print("You can ride the roller coaste and you have to pay $12")
  wants_photo = input("Do you want a photo taken? Y or N.")
  if wants_photo == "Y":
    bill += 3
  print(f"You final bill is {bill}")
else:
    print("Sorry, you have to grow taller before you can ride")

# # Write a program for pizza order.

print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Dou you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
bill = 0
if size == "S":
  bill = 15
  print("You have to pay $15")
  if add_pepperoni == "Y":
    print("Pepperoni for small size pizza is +$2")
    bill += 2
    if extra_cheese == "Y":
      bill += 1
      print("Extra cheese for any size pizza is +$1")
    print(f"Your final bill is {bill}")
if size == "M":
  bill = 20
  print("You have to pay $20")
  if add_pepperoni == "Y":
    print("Pepperoni for medium size pizza is +$3")
    bill += 3
    if extra_cheese == "Y":
      bill += 1
      print("Extra cheese for any size pizza is +$1")
    print(f"Your final bill is {bill}")
if size == "L":
  bill = 25
  print("You have to pay $25")
  if add_pepperoni == "Y":
    print("Pepperoni for large size pizza is +$3")
    bill += 3
    if extra_cheese == "Y":
      bill += 1
      print("Extra cheese for any size pizza is +$1")
    print(f"Your final bill is {bill}")

# Write a program for love calculator.

print("Welcome to Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
combined_string = name1 + name2
lower_case_string = combined_string.lower()
t = lower_case_string.count("t")
r = lower_case_string.count("r")
u = lower_case_string.count("u")
e = lower_case_string.count("e")
true = t + r + u + e
l = lower_case_string.count("l")
o = lower_case_string.count("o")
v = lower_case_string.count("v")
e = lower_case_string.count("e")
love = l + o + v + e
love_score = int(str(true) + str(love))
if (love_score < 10) or (love_score > 90):
  print(f"Your love score is {love_score}, you go together like coke and mentos")
if (love_score > 40) and (love_score < 50):
  print(f"Your score is {love_score} and you are alright together")
else:
  print(f"Your score is {love_score}")

# Write a programe for treasure island.
print("Welcome to Treasure Island.\n Your mission is to find the treasure.")
choice1 = input("You are at a crossroad, where do you want to go? Type 'left' or 'right'.\n")
choice2 = input("You came to a lake. There is an island in the middle of the lake. Type 'Wait' or 'Swim'.\n")
choice3 = input("You arrived at the island unharmed. There is a house with 3 doors. One red, one yelow and one blue. Which colour do you choose? 'Red', 'Yellow', 'Blue'\n")
if choice1 == 'left':
  if choice2 == 'Wait':
    if choice3 == 'Yellow':
      print("You win")
    else:
      print("Game over")
  else:
    print("Game Over")
else:
  print("Game Over")