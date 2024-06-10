#Write a program that prints some notes from previous lesson using what you have learned about python print function.
print("Day 1 - Python Print Function")
print("The function is declared like this: ")
print("print('what to print')")

#Fix the code below
# print(Day 1 - String Manipulation")...... colan is missing on the start
# print("String Concatenation is done with the "+" sign.") .... code string code conflict
#   print('e.g. print("Hello " + "world")').... unneccessary indentation
# print(("New Lines can be created with backslashe and n.")... two open parenthasis

#Input Manipulation
print("Hello " + input("What is your name?"))

# Write a program that prints the number of characters in a user's name.
a = input("What is your name? ")
print(len(a))

# Write a program that switches the values stored in the variables a and b.
a = input("a: ")
b = input("b: ")
c = a
a = b
b = c
print("a = ",a)
print("b = ",b)

# Write a program that generates a band name.
print("Welcome to the Band Name Generator.")
cityname = input("What's the name of the city you grew up in?\n")
petname = input("What's your pet's name?\n")
print("Your band name could be " + cityname + " " + petname)