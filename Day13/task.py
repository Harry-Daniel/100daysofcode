# def my_function():
#     for i in range(1,21):
#         if i== 20:
#             print("You got it")

# my_function()

# Describe the Problem - Write your answers as comments:
# 1. What is the for loop doing
# 2. When is the function meant to print "You got it"?
# 3. What are your assumptions about the value of i?

# year = int(input("What's your year of birth "))

# if year> 1980 and year<1994:
#     print("You are a millennial")
# elif year>= 1994 :
#     print("You are a Gen Z")
# try:
#     age= int(input("How old are you?"))
# except ValueError:
#     print("You have typed in an invalid number, please try agin with a numeric response like 15")
#     age= int(input("How old are you?"))
# if age>18:
#     print(f"You can drive at age {age}.")

words_per_page = 0

pages=int(input("Number of words per page: "))
words_per_page = int(input("Number of words per page: "))
total_words= pages * words_per_page
print(total_words)