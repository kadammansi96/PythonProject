# # file not found error
# # with open("aa.txt") as file:
# #     data = file.read()
# # FileNotFoundError: [Errno 2] No such file or directory: 'aa.txt'
#
# try:
#     file = open("a_file.txt")
#     a_dict = {"key" : "value"}
#     print(a_dict["shfuemfhd"])
# except FileNotFoundError:
#     file = open("a_file.txt", "w")
#     file.write("Something")
# except KeyError as errormessage:
#     print(f"That key {errormessage} not exists")
# else:
#     content = file.r()
#     print(content)
# finally:
#     # file.close()
#     # print("file was closed")
#     raise TypeError("This is an error that is made up")

# """Example for raise"""

# height = float(input("Height : "))
# weight = int(input("Weight : "))
#
# if height > 3:
#     raise ValueError("Human height should be not more than 3 mtrs")
#
# bmi = weight/ height ** 2
# print(bmi)

# KeyError

# a_dict = {"key": "value"}
# print(a_dict["non_existence_key"])
# KeyError: 'non_existence_key'

# KeyError Handling

facebookPost = [
    {"likes": 21, "Comments": 2},
    {"likes": 13, "Comments": 2, "Share": 1},
    {"likes": 33, "Comments": 8, "Share": 3},
    {"Comments": 4, "Share": 2},
    {"Comments": 1, "Share": 1},
    {"likes": 19, "Comments": 3},
]
totalLikes = 0

for post in facebookPost:
    try:
        totalLikes = totalLikes + post["likes"]
    except KeyError:
        pass


# IndexError

# fruit_list = ["Apple", "Mango", "Banana"]
# print(fruit_list[3])
# IndexError: list index out of range

# Index Error handling

fruit_list = ["Apple", "Mango", "Banana"]

def makepie(index):
    try:
        fruits = fruit_list[index]
    except IndexError:
        print("Fruit pie")
    else:
        print(fruits + "pie")

makepie(4)


# TypeError

# text = "abc"
# print(text + 5)
# TypeError: can only concatenate str (not "int") to str

