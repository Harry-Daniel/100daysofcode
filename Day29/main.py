from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website_name=entry_website.get()
    email_u_name=entry_email_uname.get()
    password=entry_password.get()
    data="|".join([website_name,email_u_name,password+'\n'])
    with open(f"Day29/password.txt",mode="a") as file:
        file.write(data)

    entry_password.delete(0,END)
    entry_email_uname.delete(0,END)
    entry_website.delete(0,END)





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
entry_website.grid(column=1, row=1, columnspan=2, sticky="EW")
entry_website.focus()
entry_email_uname = Entry()
entry_email_uname.grid(column=1, row=2, columnspan=2, sticky="EW")
entry_email_uname.insert(0,'hayiborkomla@gmail.com')
entry_password = Entry()
entry_password.grid(column=1, row=3, sticky="EW")

# Buttons
 
generate_btn = Button(text="Generate Password")
generate_btn.grid(column=2, row=3, sticky="EW")
 
add_btn = Button(text="Add", width=35, command=save)
add_btn.grid(column=1, row=4, columnspan=2, sticky="EW")
 
mainloop()


window.mainloop()