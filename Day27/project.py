from tkinter import *

window= Tk()
window.title("Mile to Km Converter")
window.minsize(width=100, height=100)
window.config(padx=50,pady=50)



# Input field
input = Entry(width=10)
input.grid(column=1,row=0)

# Mile label
mile_label=Label(text="Miles",font=("Arial",12,"bold"))
mile_label.grid(column=2,row=0)

# is equal to label
is_equal_label=Label(text="is equal to",font=("Arial",12,"bold"))
is_equal_label.grid(column=0,row=1)

#  km value
km_value_label=Label(text=0,font=("Arial",12,"bold"))
km_value_label.grid(column=1,row=1)


#  km v
km_label=Label(text="km",font=("Arial",12,"bold"))
km_label.grid(column=2,row=1)

# Calculate button
def button_clicked():
    km_value_label['text']=round(int(input.get())*1.60934)

button= Button(text='Click me', command=button_clicked)
button.grid(column=2,row=2)


window.mainloop()