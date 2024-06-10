# List accessing with for loop

# numbers = [1, 2, 3]
# new_list = []
# for num in numbers:
#     add_1 = num + 1
#     new_list.append(add_1)
# print(new_list)

# Same example with list comprehension

# numbers = [1, 2, 3]
# new_list = [num + 1 for num in numbers]
# print(new_list)

# example with string data for list comprehension

# name = "Mansi"
# new_list = [letter for letter in name]
# print(new_list)

# Example with range function

# new_list = [num + num for num in range(1, 5)]
# print(new_list)

# Eg with conditional list comprehension

# names = ["Mansi", "Pratik", "Ketaki", "Yashasvi", "Shashwati", "Dhanu"]
# new_list = [name for name in names if len(name) < 6]
# print(new_list)

# Eg : Write a code to create a list called squared_numbers using list comprehension

# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# squared_numbers = [num**2 for num in numbers]
# print(squared_numbers)

# Eg : Write a code to create a list called result which contains only even numbers
# using list comprehension

# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# result = [num for num in numbers if num % 2 == 0]
# print(result)

# Write your code above 👆
# with open("file1.txt") as file1:
#     file_1_data = file1.readlines()
#
# with open("file2.txt") as file2:
#     file_2_data = file2.readlines()
# result = [int(num) for num in file_1_data if num in file_2_data]
# print(result)




