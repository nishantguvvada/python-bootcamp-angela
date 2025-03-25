# with open("weather_data.csv", mode="r") as file:
#     csv_data = file.readlines()

# print(csv_data)

# import csv

# with open("weather_data.csv", mode="r") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         print(row)
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))

# print(temperatures)

import pandas as pd

# data = pd.read_csv("weather_data.csv")
# data_dict = data.to_dict()
# print(type(data_dict))

# print(data["temp"].max())

# print(data[data.temp == data.temp.max()])

data = pd.read_csv("Squirrel_Data.csv")
grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
cinnamon_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrels_count, cinnamon_squirrels_count, black_squirrels_count]
}

df = pd.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")