
# try:
#     file = open("Day30/a_file.txt")
#     a_dictionary={"key": "value"}
#     print(a_dictionary["key"])
# except FileNotFoundError:
#     file=open("Day30/a_file.txt","w")
#     file.write("something in here")
# except KeyError as error_Message:
#     print(f"That key {error_Message} does not exist")
# else:
#     content= file.read()
#     print(content)
# finally:
#     raise TypeError("This is a made up error")

height= float(input("height: "))
weight = int(input("weight: "))

if height>3:
    raise ValueError("Human Height should not be over 3 meters")

bmi = weight / height**2

print(bmi)