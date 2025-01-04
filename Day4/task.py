import random
# import my_module
# print(my_module.my_favourite_number)

# random_integer=random.randint(1,10)
# print(random_integer)

# random_number_0_to_1= random.random()*10
# print(random_number_0_to_1)


# random_float= random.uniform(1,10)
# print(random_float)

# random_number=random.randint(0,1)

# if random_number%2==0:
#     print("Heads")
# else:
#     print("Tails")


# states_of_america=["Delaware","Pennsylvania","Nebraska"]
# states_of_america[1]="Pencilvania"

# states_of_america.extend(["Mawukoland","Mmabillaland"])
# print(states_of_america)

random_friend_index= random.randint(0,4)
friends=["Alice", "Bob","Charlie","David","Emanuel"]
print(friends[random_friend_index])
# OR
print(random.choice(friends))