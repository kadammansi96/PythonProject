# fruits = ["apple", "banana", "cherry"]
# for fruit in fruits:
#   print(fruit)
#   print(fruit + " pie")

# Write a program to calulate avergae height of students from a list of heights.

# student_heights = input("Input a list of student heights").split()
# for n in range(0, len(student_heights)):
#   student_heights[n] = int(student_heights[n])
# print(student_heights)

# total_height = 0
# for height in student_heights:
#   total_height += height

# number_of_students = 0
# for student in student_heights:
#   number_of_students += 1

# average_height = round(total_height / number_of_students)
# print(average_height)

# Write a program that calculates the highest score from a list of scores.

# student_score = input("Input a list of student score").split()
# for n in range(0, len(student_score)):
#   student_score[n] = int(student_score[n])
# print(student_score)
# highest_score = 0
# for score in student_score:
#   if score > highest_score:
#     highest_score = score
# print(f"The highest score in the class is: {highest_score}")

# Write a program that calculates the sum of all the even numbers from 1 to 100.

# total = 0
# for number in range(0, 101, 2):
#   total += number
# print(total)

# Write a program that automatically prints the solution to the FizzBuzz game.

# for number in range(1, 101):
#   if number % 3 == 0 and number % 5 == 0:
#     print("FizzBuzz")
#   elif number % 3 == 0:
#     print("Fizz")
#   elif number % 5 == 0:
#     print("Buzz")
#   else:
#     print(number)

# Write a program that generates a password based on user input.

import random
letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','#','$','%','&','(',')','*','+']
print("Wecome to the PyPassword Generator")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))
password = ""

# Easy way
# for char in range(0, nr_letters):
#   password += random.choice(letter)
# for num in range(0, nr_numbers):
#   password += random.choice(numbers)
# for symb in range(0, nr_symbols):
#   password += random.choice(symbols)
# print(password)

# Hard way

password_list = []
for char in range(0, nr_letters):
  password_list.append(random.choice(letter))
for char in range(0, nr_numbers):
  password_list.append(random.choice(numbers))
for char in range(0, nr_symbols):
  password_list.append(random.choice(symbols))
print(password_list)
random.shuffle(password_list)
print(password_list)
for char in password_list:
  password += char
print(f"Your password is: {password}")