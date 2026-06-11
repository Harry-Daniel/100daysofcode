from tkinter import *
THEME_COLOR = "#375362"
WHITE="#ffffff"
BLACK="#000000"

class QuizInterface:

    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.minsize(width=300,height=250)
        self.window.config(pady=20,padx=20,bg=THEME_COLOR)
        
        # score
        self.my_score=Label(text="Score: 10",font=("Arial",10),bg=THEME_COLOR,fg=WHITE)
        self.my_score.grid(column=1,row=0)
      
        #canvas 
        self.canvas=Canvas(bg=WHITE, width=300, height=250)
        self.question_text=self.canvas.create_text(150,
    125,width=280,text="Amazon acquired Twitch in August 2014 for $970 million dollars.",font=("Arial",20,"italic"),fill=THEME_COLOR)
        self.canvas.grid(column=0,row=1, columnspan=2,pady=50)
        # Buttons
        false_image=PhotoImage(file="day34/quizzler-app-start/images/false.png",width=100,height=100)
        self.false_button=Button(image=false_image,highlightthickness=0)
        self.false_button.grid(column=1,row=2)

        true_image=PhotoImage(file="day34/quizzler-app-start/images/true.png",width=100,height=100)
        self.true_button=Button(image=true_image,highlightthickness=0)
        self.true_button.grid(column=0,row=2)



        self.window.mainloop()
