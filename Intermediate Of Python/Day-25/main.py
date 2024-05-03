# with open("weather-data.csv", "r") as weather:
#     weather_data = weather.readlines()
#     line_list = []
#     for line in weather_data:
#         line_list.append(line.split(","))
#     print(line_list)
# import csv
# with open("weather-data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperature = []
#     for row in data:
#         if row[1] != 'temp':
#             temp = row[1]
#             temperature.append(int(temp))
#     print(temperature)
# import pandas
# data = pandas.read_csv("weather-data.csv")
# print(data)
# temp = data["temp"]
# temp_list = temp.to_list()
# print(temp_list)
# average = (sum(temp_list)) / len(temp_list)
# print(f"Average temperature is : {round(average, 2)}")

# print(data[data.temp == data.temp.max()])
# monday = data[data.day == "Monday"]
# temp_c = int(monday.temp)
# temp_ferhenhit = temp_c * 9/5 + 32
# print(temp_ferhenhit)

# data_dict = {
#     "students": ["Aakash", "Bhavesh", "Bharat", "Vinay", "Ram"],
#     "marks": [98, 87, 77, 56, 90]
# }
# data_panda = pandas.DataFrame(data_dict)
# print(data_panda)

import pandas
data = pandas.read_csv("Squirrel_Data.csv")
gray_list = len(data[data["Primary Fur Color"] == "Gray"].X)
cinnamon_list = len(data[data["Primary Fur Color"] == "Cinnamon"].X)
black_list = len(data[data["Primary Fur Color"] == "Black"].X)

data_dict = {
    "Color": ["Gray", "Cinnamon", "Black"],
    "Number": [gray_list, cinnamon_list, black_list]
}
data_frame = pandas.DataFrame(data_dict)
data_frame.to_csv("data_dict_frame.csv")
