# Eg for dictionary comprehension for looping through a list

# import random
# names = ["Mansi", "Pratik", "Tiya", "Shashwati", "Prachi"]
# student_score = {student: random.randint(20, 90) for student in names}
# print(student_score)

# Eg for dictionary comprehension for looping through a dictionary

# student_score = {
#     'Mansi': 63,
#     'Pratik': 43,
#     'Tiya': 63,
#     'Shashwati': 81,
#     'Prachi': 74
# }
# passed_students = {student: score for (student, score) in student_score.items() if score >= 60}
# print(passed_students)

# Using Dictionary comprehension, create a dictionary called result that takes each
# word in the given sentence and calculate teh number of letters in each word

# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# result = {word: len(word) for word in sentence.split()}
# print(result)

# Using Dictionary comprehension, create a dictionary called weather_f that
# that takes each temperature in degree Celsius and convert it to fehrenheight

# weather_c = {
#     "Monday": 12,
#     "Tuesday": 14,
#     "Wednesday": 15,
#     "Thursday": 14,
#     "Friday": 21,
#     "Saturday": 22,
#     "Sunday": 24,
# }
# weather_f = {days: (temp_c * 9/5 + 32) for (days, temp_c) in weather_c.items()}
# print(weather_f)

# How to iterate over a Pandas Dataframe

student_dict = {
    "students": ["Angela", "James", "Lily"],
    "score": [56, 78, 98],
}
# Looping through dictionary
for (key, value) in student_dict.items():
    print(key, value)

# Creating a table using dataframe
import pandas
student_dataframe = pandas.DataFrame(student_dict)
print(student_dataframe)

# Looping through rows of a Dataframe
for (index, row) in student_dataframe.iterrows():
    print(index)
    # print(row)
    # print(row.students)
    # print(row.score)






