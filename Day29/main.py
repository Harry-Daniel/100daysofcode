from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #



window=Tk()
window.title("Password Manager")
window.config(padx=20,pady=20)

canvas= Canvas(width=200, height=200)

lockImage=PhotoImage(file="Day29/logo.png")
canvas.create_image(100,100,image=lockImage)
canvas.pack()




window.mainloop()