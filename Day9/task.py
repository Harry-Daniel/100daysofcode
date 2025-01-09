programming_dictionary={
    "Bug":"An error in a program that prevents the program from executing correctly.",
    "Function":"A piece of code that you can easily call over and over.",
    
}

print(programming_dictionary)

programming_dictionary["Loop"]="The action of doing somthig over and over again"
print(programming_dictionary)

empty_dictionary={}

# Wipe existing dictionary

# programming_dictionary={}

# print(programming_dictionary)


# Edit an item in a dictionary

programming_dictionary["Bug"]= "A moth in your computer"

print(programming_dictionary)


# Loop throufh a dictionaruy:
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])