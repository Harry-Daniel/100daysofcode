alphabet=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']




def caesar(original_text,shift_amount,direction):
    new_text=''
    if direction == 'encode' or direction =='decode':
        for letter in original_text:
            

            if letter in alphabet:
                # Find the index of the letter in the text 
                letter_index=alphabet.index(letter)
                # After finding index , find the new letter by (adding shift amount to the old letter index)modulo 26 to make sure the new index is in range and finding the new letter from the alphabet list using indices
                if direction=='encode':
                    new_text+=alphabet[(letter_index+shift_amount)%26]
                elif direction=='decode':
                    new_text+=alphabet[(letter_index-shift_amount)%26]
            else:
                new_text+=letter
            
        print(f"Here is the result: {new_text}")

    else:
        print("Wrong Input. Choose a direction. encode or decode")





keep_going=True
while keep_going== True:
    direction= input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()

    text= input("Type your message:\n").lower()
    shift=int(input("Type the shift number:\n"))

    caesar(text,shift,direction)
    
    continue_encoding=input("Keep going? Type 'yes' or 'no'.\n").lower()
    if continue_encoding== 'no':
        keep_going=False
        print("Goodbye")

