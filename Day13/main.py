# #####################Debugging#########################

# Describe problem 
# def my_function():
#   for i in range(1, 20):
#     if i == 20:
#       print("You got it")
# my_function()
# Solution:
# def my_function():
#   for i in range(1, 21):
#     if i == 20:
#       print("You got it")
# my_function()



# Reproduce the bug
# from random import randint
# dice_image = ["❶", "❷", "❸", "❹", "❺", "❻"] #lists start counting from 0
# dice_number = randint(1, 6) #and here in range we started from 1, which it starts displaying from index 1 and not 0 and we need to end at index 5 not on index 6
# print(dice_image[dice_number])
# # Solution
# dice_image = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_number = randint(0, 5)
# print(dice_image[dice_number])


# Play computer
# year = int(input("Whats the year of your birth?"))
# if year > 1980 and year <= 1994:
#   print("You are a millenial.")
# elif year >= 1995:
#   print("You are Gen Z")


# Fix the errors
# age = input("How old are you?") #here we need to convert the input to int
# if age > 18:
# print("You can drive at age {age}.") # indentation is missing and f string is missing
# Solution:
# age = int(input("How old are you?"))
# if age > 18:
#   print(f"You can drive at age {age}.")


# Print is your friend
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page = int(input("Number of word per page? "))
# total_word = pages * word_per_page
# print(pages)
# print(word_per_page)
# print(total_word)


# Use a debugger
# def mutate(a_list):
#   b_list = []
#   for items in a_list:
#     new_item = items * 2
#   b_list.append(new_item)
#   print(b_list)# Output here is displayed is directly end result, whereas we are expecting output to be [26, 52, 78, 104]
# Solution
# def mutate(a_list):
#   b_list = []
#   for items in a_list:
#     new_item = items * 2
#     b_list.append(new_item)
#     print(b_list) # Once the b_list is inside the for loop, it will print the list everytime the for loop runs as expected [26, 52, 78, 104]]


# Debugging odd or even code
# number = int(input("Enter a number to check for even or odd"))
# if number % 2 = 0: # assigment operator is used
#   print("This is an even number")
# else: 
#   print("This is odd number")
# Solution
# number = int(input("Enter a number to check for even or odd"))
# if number % 2 == 0: 
#   print("This is an even number")
# else: 
#   print("This is odd number")