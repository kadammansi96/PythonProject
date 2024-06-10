from art import logo
# Functions with output

# def format_name(f_name, l_name):
#   print(f_name.title())
#   print(l_name.title())
# format_name("angela", "ANGELA")

# Functions with output

# def format_name(f_name, l_name):
#   formatted_f_name = f_name.title()
#   formatted_l_name = l_name.title()
#   return f"{formatted_f_name} {formatted_l_name}"
# formatted_string = format_name("MansI", "PRaTiK")
# print(formatted_string)

# Leap year function program

# def is_leap(year):
#   if year % 4 == 0:
#     if year % 100 == 0:
#       if year % 400 == 0:
#         return True
#       else:
#         return False
#     else:
#       return True
#   else:
#     return False
# def days_in_month(year, month):
#   if month > 12 or month < 1:
#     return "Invalid month"
#   month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#   if is_leap(year) and month == 2:
#     return 29
#   return month_days[month - 1]

# year = int(input("Enter a year: \n"))
# month = int(input("Enter a month: \n"))
# days = days_in_month(year, month)
# print(days)

# write a program to design a calculator

# # # Add
# def add(n1, n2):
#   return n1 + n2

# # # Subtract
# def subtract(n1, n2):
#   return n1 - n2

# # Multiple
# def multiply(n1, n2):
#   return n1 * n2

# # Divide
# def divide(n1, n2):
#   return n1 / n2 

# operations = {
#   "+" : add,
#   "-" : subtract,
#   "*" : multiply,
#   "/" : divide,
# }

# num1 = int(input("Whats the first number?: \n"))
# num2 = int(input("Whats the second number?: \n"))
# for symbols in operations:
#   print(symbols)
# operation_symbol = input("Pick an operation from the line above: \n")

# calculation_function = operations[operation_symbol]
# answer = calculation_function(num1, num2)

# print(f"{num1} {operation_symbol} {num2} = {answer}")

# # Write a program to design a calculator for multiple operations

# # # Add
# def add(n1, n2):
#   return n1 + n2

# # Subtract
# def subtract(n1, n2):
#   return n1 - n2

# # Multiple
# def multiply(n1, n2):
#   return n1 * n2

# # Divide
# def divide(n1, n2):
#   return n1 / n2 

# operations = {
#   "+" : add,
#   "-" : subtract,
#   "*" : multiply,
#   "/" : divide,
# }

# num1 = int(input("Whats the first number?: \n"))  
# for symbols in operations:
#   print(symbols)
# should_continue = True
# while should_continue:
#   operation_symbol = input("Pick an operation: \n")
#   num2 = int(input("Whats the next number?: \n"))
#   calculation_function = operations[operation_symbol]
#   answer = calculation_function(num1, num2)
#   print(f"{num1} {operation_symbol} {num2} = {answer}")
#   if input(f"Type 'y' to continue calculating with {answer} or type 'n' to exit: ") == "y":
#     num1 = answer
#   else: 
#     should_continue = False

# # Write a program to design a calculator for multiple times of use of calculator

# # Add
# def add(n1, n2):
#   return n1 + n2

# # Subtract
# def subtract(n1, n2):
#   return n1 - n2

# # Multiple
# def multiply(n1, n2):
#   return n1 * n2

# # Divide
# def divide(n1, n2):
#   return n1 / n2 

# operations = {
#   "+" : add,
#   "-" : subtract,
#   "*" : multiply,
#   "/" : divide,
# }

# def calculator():
#   print(logo)
#   num1 = float(input("Whats the first number?: \n"))  
#   for symbols in operations:
#     print(symbols)
#   should_continue = True
#   while should_continue:
#     operation_symbol = input("Pick an operation: \n")
#     num2 = float(input("Whats the next number?: \n"))
#     calculation_function = operations[operation_symbol]
#     answer = calculation_function(num1, num2)
#     print(f"{num1} {operation_symbol} {num2} = {answer}")
#     if input(f"Type 'y' to continue calculating with {answer} or type 'n' to start a new calculation: ") == "y":
#       num1 = answer
#     else: 
#       should_continue = False
#       calculator()

# calculator()