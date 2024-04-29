# # Write a programe that adds the digits in a 2 digit number. e.g. if the input was 35, then the output should be 3 + 5 = 8
two_digit_number = input("Type a two digit number: ")
first_digit = two_digit_number[0]
second_digit = two_digit_number[1]
result = int(first_digit) + int(second_digit)
print(result)

# # write a program that calculates the Body Mass Index (BMI) from a user's weight and height.
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
bmi = int(weight) / float(height) ** 2
bmi_as_int = int(bmi)
print(bmi_as_int)

# # create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old.

age = int(input("What is your current age? "))
years_left = 90 - age
days_left = years_left * 365
weeks_left = years_left * 52
month_left = years_left * 12
print("You have ", days_left, "days" , weeks_left, "weeks" , month_left, "months left")

# Write a program to create a tip calculator

print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15?"))
people = int(input("How many people to split the bill?"))
bill_with_tip = tip / 100 * bill + bill
print(bill_with_tip)
bill_after_split = bill_with_tip / people
print(bill_after_split)
