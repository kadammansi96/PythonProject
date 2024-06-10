# Reading the content from file
# with open("my_file.txt") as file:
#     contents = file.read()
#     print(contents)
#     file.close()
#

# Writing a completely new content onto file

# with open("my_file.txt", mode= "w") as file:
#     file.write("New text.")


# Appending a new content onto file

# with open("my_file.txt", mode= "a") as file:
#     file.write("\nNew Text")


# Writing onto new file from scratch

# with open("newFile.txt", mode= "w") as file:
#     file.write("Hi")


# Reading the content from file which is stored to some other location
# with open("/Users/Dell/Desktop/my_file.txt") as file:
#     contents = file.read()
#     print(contents)
#     file.close()

with open("../../Desktop/my_file.txt") as file:
    content = file.read()
    print(content)

