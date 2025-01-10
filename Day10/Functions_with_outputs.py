

# def format_name(fname,lname):
#     formatted_name= fname.title()+' '+lname.title()

#     return formatted_name

# formatted_string=format_name("MaWUko", "HAYIBOR")

# print(formatted_string)

# ouput= len("Mawuko")

def function_1(text):
    return text+text

def function_2(text):
    return text.title()

output = function_2(function_1("hello"))
print(output)