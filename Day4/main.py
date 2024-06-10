import random
# import mymodule

# # random_integer = random.randint(1, 10)
# # print(random_integer)
# random_floatnum = random.random()
# print(random_floatnum)
# # print(mymodule.pi)

# # Write a program to virtual coin toss.

random_side = random.randint(0, 1)
if random_side == 1:
  print("Heads")
else:
  print("Tails")

# Write a program which will select a random name from a list of names. The person selected will have to pay for everybody's food bill.

name_string = input("Give me everybody's names, separated by a comma. ")
names = name_string.split(",")
print(names)
random_coice = random.randint(0, len(names)-1)
print(f"{names[random_coice]} is going to buy the meal today!")

# Write a program which will mark a spot with an X.

row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure?")
horizontal = int(position[0])
vertical = int(position[1])
selected_row = map[vertical - 1]
selected_row[horizontal-1] = 'X'
print(f"{row1}\n{row2}\n{row3}")

