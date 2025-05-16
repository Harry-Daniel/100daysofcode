from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"











# --------------------------------------UI SETUP------------------------------------#

window= Tk()
window.title("Flash Card")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)

canvas= Canvas(width=800, height=526,bg=BACKGROUND_COLOR,highlightthickness=0)

card_front=PhotoImage(file="Day31/images/card_front.png")
canvas.create_image(400,263,image=card_front)
canvas.create_text(400,150,text="Title", font=("Ariel",40,"italic"))
canvas.create_text(400,263, text="word",font=("Ariel",60,"bold"))
canvas.grid(column=0,row=0, columnspan=2)


cross_image= PhotoImage(file="Day31/images/wrong.png")
unknown_button =Button(image=cross_image, highlightthickness=0)
unknown_button.grid(row=1, column=0)

check_image=PhotoImage(file="Day31/images/right.png")
known_button= Button(image=check_image,highlightthickness=0)
known_button.grid(row=1,column=1)



window.mainloop()