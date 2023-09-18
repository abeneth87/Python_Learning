import pandas as pd
import numpy as np

data = pd.read_csv("weather_data.csv")
# print(type(data))
# print(type(data["day"]))

data_dict = data.to_dict()
print(data_dict)

temp_list = data["temp"].to_list()
print(np.average(temp_list))  # Using numpy function
print(data["temp"].mean())  # Using panda series

print(np.max(temp_list))
print(data["temp"].max())

print(data[data.day == "Monday"])
print(data[data.temp == data["temp"].max()])

monday = data[data.day == "Monday"]
monday_temp = monday.temp[0]
monday_temp_f = monday_temp * 9/5 + 32
print(monday_temp_f)