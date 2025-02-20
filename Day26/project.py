

import pandas
data_set = pandas.read_csv("Day26/nato_phonetic_alphabet.csv")

#Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    # pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
nato_alphabet={row.letter:row.code for (index,row) in data_set.iterrows()}
# print(nato_alphabet)
# {"A": "Alfa", "B": "Bravo"}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

user_input= input("Input:").upper()

nato_list=[nato_alphabet[letter] for letter in user_input]
print(nato_list)