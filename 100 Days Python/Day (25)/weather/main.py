#
# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

import csv

with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)
    temperatures = []
    for item in data:
        if item[1] != "temp":
            temperatures.append(int(item[1]))
    print(temperatures)

