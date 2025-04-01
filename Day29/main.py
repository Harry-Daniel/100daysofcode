from tkinter import *
from tkinter import messagebox
from random import choice,randint,shuffle
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
    password = entry_password.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


    password_list = []

    password_letters=[choice(letters) for _ in range(randint(8, 10))]
    password_symbols=[choice(symbols) for _ in range(randint(2, 4))]
    password_numbers=[choice(numbers) for _ in range(randint(2, 4))]
    password_list= password_letters+password_numbers+password_symbols



    shuffle(password_list)

    password="".join(password_list)

    entry_password.insert(0,password) 
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website=entry_website.get()
    email=entry_email_uname.get()
    password=entry_password.get()
    new_data={website:{
        'email':email,
        'password': password,
    }}
    

    if len(website)<1 or len(password)<1:
        messagebox.showerror(title="Empty Fields",message="No Field should be left empty")
    else:
        try:
            with open(f"Day29/password.json",mode="r") as file:
                # Reading data
                data=json.load(file)
                data.update(new_data)
        except FileNotFoundError:
            with open(f"Day29/password.json",mode="w") as file:
                # Create data fle if file doesn't exist
                json.dump(new_data,file,indent=4)
        else:        
            with open(f"Day29/password.json",mode="w") as file:
                # Saving updated data
                json.dump(data,file,indent=4)
        finally:
            entry_password.delete(0,END)
            entry_website.delete(0,END)


# ------------------------------Search--------------------------------------------------- #

def find_password():
    website=entry_website.get()
    
    try:
        with open(f"Day29/password.json",mode="r") as file:
            # Reading data
            data=json.load(file)
            # data.update()
            print(data[f'{website}'])
    except FileNotFoundError:
        messagebox.showerror(title="File not found",message="No data file was found")
    except KeyError:
        messagebox.showerror(title="Password not found",message="There is no password for this website")
    else:        
        messagebox.askokcancel(title=website,message=f"These are the details:\n Email:{data[f'{website}']['email']}\n Password: {data[f'{website}']['password']} ")
    

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Generator")
window.config(padx=20, pady=20)
 
canvas = Canvas(width=200, height=200)
tomato_img = PhotoImage(file="Day29/logo.png")
canvas.create_image(100, 100, image=tomato_img)
canvas.grid(column=1, row=0)
 
#  Labels
label_website=Label(text="Website:")
label_website.grid(column=0, row=1)
 
label_email_uname = Label(text="Email/Username:")
label_email_uname.grid(column=0, row=2)
 
 
label_password = Label(text="Password:")
label_password.grid(column=0, row=3)
 
#  Entries
entry_website = Entry()
entry_website.grid(column=1, row=1,  sticky="EW")
entry_website.focus()
entry_email_uname = Entry()
entry_email_uname.grid(column=1, row=2, columnspan=2, sticky="EW")
entry_email_uname.insert(0,'hayiborkomla@gmail.com')
entry_password = Entry()
entry_password.grid(column=1, row=3, sticky="EW")

# Buttons
 
search_btn = Button(text="Search", command=find_password)
search_btn.grid(column=2, row=1, sticky="EW")
generate_btn = Button(text="Generate Password", command=generate_password)
generate_btn.grid(column=2, row=3, sticky="EW")
 
add_btn = Button(text="Add", width=35, command=save)
add_btn.grid(column=1, row=4, columnspan=2, sticky="EW")
 
mainloop()


window.mainloop()