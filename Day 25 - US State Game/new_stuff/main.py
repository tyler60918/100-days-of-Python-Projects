# # data = []
# # with open("weather_data.csv") as data_file:
# #     data = data_file.readlines()

# # print(data)

# # import csv

# # with open("Weather_data.csv") as data_file:
# #     data = csv.reader(data_file)
# #     temperatures = []
# #     for row in data:
# #         if row[1] != "temp":
# #             temperatures.append(int(row[1]))
        
# #     print(temperatures)

import pandas

data = pandas.read_csv("new_stuff/weather_data.csv")

# temperatures = data["temp"].to_list()
# average = sum(temperatures) / len(temperatures)
# print(average)

# # OR

# # Get data in column
# print(data["temp"].mean())

# print(data["temp"].max())

# print(data["condition"])
# print(data.condition)

# # Get data in row
# print(data[data.day == "Monday"])

# # Get row where that day has the highest temp
# print(data[data.temp == data.temp.max()])

# # Get the temperature for Monday and convert it to Celsius
monday = data[data.day == "Monday"]
print(monday)
monday_temp_f = monday.temp[0]  * (9/5) + 32
# print(monday_temp_f)

# # Create a DataFrame from scratch
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")

import pandas

data = pandas.read_csv("new_stuff/2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20260611.csv")
gray_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])

data_dict_export = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrels_count, red_squirrels_count, black_squirrels_count]
}
data = pandas.DataFrame(data_dict_export)
data.to_csv("new_stuff/squirrel_count.csv")

