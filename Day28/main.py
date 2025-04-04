from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
SEC_IN_MIN=60
reps=1
timer=None
# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text,text="00:00")
    title_label.config(text="TIMER")
    checksigns.config(text="")
    global reps
    reps=1


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    work_sec=WORK_MIN*SEC_IN_MIN
    short_break_sec= SHORT_BREAK_MIN*SEC_IN_MIN
    long_break_sec= LONG_BREAK_MIN*SEC_IN_MIN

    if reps%2==1:
        title_label.config(fg=GREEN,text="WORK")
        count_down(work_sec)
    elif reps == 8:
        title_label.config(fg=RED,text="BREAK")
        count_down(long_break_sec)
    elif reps%2==0:
        title_label.config(fg=PINK,text="BREAK")
        count_down(short_break_sec)

    # If reps hasn't reached 8 continue adding, once it reaches 8 reps start from 1
    if reps<8:
        reps+=1
    else:
        reps=1





# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min= math.floor(count/60)
    count_sec=count%60
    if count_sec<10:
        count_sec=f"0{count_sec}"



    canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")
    global timer
    if count>0:
       timer= window.after(1000,count_down,count-1)
    else:
        start_timer()
        marks=""
        work_sessions=math.floor(reps/2)
        for _ in range(work_sessions):
            marks+="✔️"
        checksigns.config(text=marks)



        

# ---------------------------- UI SETUP ------------------------------- #

window=Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg=YELLOW)


title_label=Label(text="TIMER",font=(FONT_NAME,50),bg=YELLOW,fg=GREEN)
title_label.grid(column=1,row=0)

canvas= Canvas(width=200, height=224,bg=YELLOW,highlightthickness=0)

tomato_img=PhotoImage(file="Day28/tomato.png")
canvas.create_image(100,112,image=tomato_img)
timer_text=canvas.create_text(100,130,text='00:00', fill="white", font=(FONT_NAME,35,"bold"))
canvas.grid(column=1,row=1)

start=Button(text='Start',command=start_timer)
start.grid(column=0,row=2)

reset=Button(text='Reset',command=reset_timer)
reset.grid(column=3,row=2)


checksigns=Label(bg=YELLOW,fg=GREEN)
checksigns.grid(column=1,row=3)







window.mainloop()