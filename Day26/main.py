# numbers =[1,2,3]
# new_numbers=[item+1 for item in numbers]
# print(new_numbers)

# name= "Mawuko"

# letter_list=[letter for letter in name]

# print(letter_list)


# doubled=[item*2 for item in range(1,5)]

# print(doubled)
# import random

# names=['Alex','Beth',"Caroline","Dave","Eleanor","Freddie"]

# students_score={
#     student:random.randint(1,100) for student in names
# }
# print(students_score)

# passed_students={student:mark for (student,mark) in students_score.items() if mark > 50}

# print(passed_students)

student_dict={
    "student":["Angela","James","Lily"],
    "score": [56,76,98]
}

# for (key,value) in student_dict.items():
#     print(value)

import pandas

student_data_frame=pandas.DataFrame(student_dict)
print(student_data_frame)

# Loop through data frame

# for (key,value) in student_data_frame.items():
#     print(value)

# Loop thorugh rows of a data frame
for (index,row) in student_data_frame.iterrows():
    if row.student == 'Angela':
        print(row.score)