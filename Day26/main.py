# numbers =[1,2,3]
# new_numbers=[item+1 for item in numbers]
# print(new_numbers)

# name= "Mawuko"

# letter_list=[letter for letter in name]

# print(letter_list)


# doubled=[item*2 for item in range(1,5)]

# print(doubled)

names=['Alex','Beth',"Caroline","Dave","Eleanor","Freddie"]

short_names=[name.upper() for name in names if len(name)>5]
print(short_names)