# # with open("002 weather-data.csv") as file:
# #     files = file.readlines()
# #     print(files)
# #
#
# # import csv
# #
# # with open("002 weather-data.csv") as data_file:
# #     data = csv.reader(data_file)
# #     temperatures = []
# #     for row in data:
# #         if row[1] != "temp":
# #             temperatures.append(int(row[1]))
# #     print(temperatures)
#
import pandas
#
# # data = pandas.read_csv("weather-data.csv")
# # print(data["temp"])
#
# # data_dict = data.to_dict()
# # print(f"data_dict : {data_dict}")
# #
# # temp_list = data["temp"].to_list()
# # print(f"temp_list : {temp_list}")
#
# # avg = sum(temp_list) / len(temp_list)
# # print(avg)
#
# # print(data["temp"].max())
# #
# # # get data in column
# # print(data["condition"])
# # print(data.condition)
# #
# # # get data in row
# # print(data[data.day == "Monday"])
#
# # get data on which day the temperature was max
# # print(data[data.temp == data["temp"].max()])
#
# # get data on particular column of particular row
# # monday = data[data.day == "Monday"]
# # print(monday.condition)
#
# # get temp from celsius to fehreneit
# # monday = data[data.day == "Monday"]
# # monday_temp = monday.temp
# # temp = (monday_temp * 9/5) + 32
# # print(temp)
#
#
# # create dataframe from scratch
#
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
# data = pandas.DataFrame(data_dict)
# # print(data)
# data.to_csv("new_data.csv")

#
# data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20240520.csv")
# gray_squirrels = len(data[data["Primary Fur Color"] == "Gray"])
# cinnamon_squirrels = len(data[data["Primary Fur Color"] == "Cinnamon"])
# black_squirrels = len(data[data["Primary Fur Color"] == "Black"])
# print(gray_squirrels, cinnamon_squirrels, black_squirrels)
#
# data_dict = {
#     "Fur color": ["Gray", "Cinnamon", "Black"],
#     "count": [gray_squirrels, cinnamon_squirrels, black_squirrels]
# }
# df = pandas.DataFrame(data_dict)
# print(df)
# df.to_csv("squirrel_count.csv")

