# import csv

# with open ("Day25/weather_data.csv") as file:
#     data=file.readlines()
#     print(data)


# with open ("Day25/weather_data.zcsv") as file:
#     data= csv.reader(file)
#     data_list=[]
#     temperatures=[]
#     for row in data:
#         data_list.append(row)
#     for data in data_list[1:]:
#         temperatures.append(int(data[1]))
#     print(temperatures)

import pandas

data=pandas.read_csv("Day25/2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20250217.csv")
# print(type(data["temp"][0]))

# data_dict=data.to_dict()

# print(data_dict)

# temp_list = data["temp"].to_list()

# print(data[data.temp==data.temp.max()])

grey= data[data['Primary Fur Color']== "Gray"]
no_grey=len(grey)

red= data[data['Primary Fur Color']== "Cinnamon"]
no_red=len(red)

black= data[data['Primary Fur Color']== "Black"]
no_black=len(black)
print(no_black)



# Create a dataframe from scratch

data_dict={
    "Fur Color":["grey","red","black"],
    "Count":[no_grey,no_red, no_black]
}

data= pandas.DataFrame(data_dict)
data.to_csv("Day25/squirrel_count.csv")
