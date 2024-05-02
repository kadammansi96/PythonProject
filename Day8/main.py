# Create a function called greet(). 
# Write three print statements inside the funtion. 
# Call the greet() function and run the code

# def greet():
#   print("Hello")
#   print("How do you do?")
#   print("Isn't the weather nice today?")
# greet()

# function that allows for input

# def greet_with_name(name):
#   print("Hello " + name)
#   print("How do you do? " + name)
#   print("Isn't the weather nice today?")
# greet_with_name("Angela")

# Functions with more than 1 input using keyword arguments

# def greet_with(name, location):
#   print("Hello " + name)
#   print(f"What is it like in {location}?")
# greet_with("Angela", "London")

# Functions with more than 1 input using keyword arguments

# def greet_with(location, name):
#   print(f"Hello {name}!")
#   print(f"What is it like in {location}?")
# greet_with(name = "Angela", location = "London")

# Write a program that calculates the number of paint cans needed to paint a wall.

# def paint_calc(height, width, cover):
#   number_of_cans = round((height * width) / cover)
#   print(f"You'll need {round(number_of_cans)} cans of paint.")
# test_h = int(input("Height of a Wall : "))
# test_w = int(input("Width of a Wall : "))
# coverage = 5
# paint_calc(height = test_h, width = test_w, cover = coverage)

# Write a program to prime number checker

# def prime_checker(number):
#   is_prime = True
#   for i in range(2, number):
#     if i % number == 0:
#       is_prime = False
#   if is_prime == True:
#     print("It's a prime number.")
#   else:
#     print("It's not a prime number.")
# n = int(input("Check this number : "))
# prime_checker(number = n)

# Write a program for ceasar ciphers

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z' ]
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt : \n")
message = input("Type your message : \n"). lower()
shift = int(input("Type the shift number : \n"))

def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  if cipher_direction == "decode":
    shift_amount *= -1
  for letter in start_text:
    position = alphabet.index(letter)
    new_position = position + shift_amount
    end_text += alphabet[new_position]
  print(f"The {cipher_direction}d text is {end_text}")

caesar(start_text = message, shift_amount = shift, cipher_direction = direction)
