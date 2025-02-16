# import csv

# with open ("Day25/weather_data.csv") as file:
#     data=file.readlines()
#     print(data)


# with open ("Day25/weather_data.csv") as file:
#     data= csv.reader(file)
#     data_list=[]
#     temperatures=[]
#     for row in data:
#         data_list.append(row)
#     for data in data_list[1:]:
#         temperatures.append(int(data[1]))
#     print(temperatures)

import pandas

data=pandas.read_csv("Day25/weather_data.csv")
print(data["temp"][0])
