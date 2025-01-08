alphabet=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction= input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()

text= input("Type your message:\n").lower()
shift=int(input("Type the shift number:\n"))


def encrypt(original_text,shift_amount):
    new_text=''
 
    for letter in original_text:
        # Find the index of the letter in the text 
        letter_index=alphabet.index(letter)
        # After finding index , find the new letter by (adding shift amount to the old letter index)modulo 26 to make sure the new index is in range and finding the new letter from the alphabet list using indices

        new_text+=alphabet[(letter_index+shift_amount)%26]
       
    print(f"Here is the encoded result: {new_text}")


encrypt(text,shift)
