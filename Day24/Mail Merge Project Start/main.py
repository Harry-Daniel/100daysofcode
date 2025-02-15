#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


with open("Day24/Mail Merge Project Start/input/Names/invited_names.txt",mode="r") as file:
    names_list=file.readlines()

for name in names_list:
    name=name.strip('\n')
   
    with open("Day24/Mail Merge Project Start/input/Letters/starting_letter.txt",mode="r") as file:
        letter=file.read()

    new_letter=letter.replace("[name]", f"{name}")
    

    with open(f"Day24/Mail Merge Project Start/Output/ReadyToSend/{name}.txt",mode="a") as file:
        file.write(new_letter)