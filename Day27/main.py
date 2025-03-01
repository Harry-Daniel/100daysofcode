from tkinter import *

window= Tk()
window.title("My first GUI Program")
window.minsize(width=500, height=300)


# Label

my_label=Label(text="I am a label",font=("Arial",24,"bold"))


my_label["text"] = "New Text"

my_label.config(text="New Text 2")
my_label.grid(column=0,row=0)
window.config(padx=20,pady=20)


# Button

def button_clicked():
    my_label['text']=input.get()

button= Button(text='Click me', command=button_clicked)
button.grid(column=1,row=1)

# New Button

new_button= Button(text="Click me")
new_button.grid(column=3,row=0)


# Entry 

input = Entry(width=10)
input.grid(column=4,row=3)

window.mainloop()

# Started hackerrank