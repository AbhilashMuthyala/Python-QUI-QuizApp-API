THEME_COLOR = "#375362"

from tkinter import *
from quiz_brain import QuizBrain

class Quizinterface():



    def __init__(self,quizbrain: QuizBrain):
        self.quiz = quizbrain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20,pady=20,bg=THEME_COLOR)
        self.canvas = Canvas(height=250,width=300,highlightthickness=0)
        self.canvas.grid(row=1,column=0,columnspan=2,padx=10, pady=10)
        self.question_text = self.canvas.create_text(150,125,text="somequestion",fill=THEME_COLOR,width=280)

        self.label = Label(text="Score: 0",fg='white',bg=THEME_COLOR,font=('Ariel','14','bold'))
        self.label.grid(row=0, column=1)

        self.my_image_true = PhotoImage(file="images/true.png")
        self.button_true = Button(image=self.my_image_true, highlightthickness=0,command=lambda: self.give_feedback('True'))

        self.button_true.grid(row=2, column=0,padx=10, pady=10)

        self.my_image_false = PhotoImage(file="images/false.png")
        self.button_false = Button(image=self.my_image_false, highlightthickness=0,command=lambda: self.give_feedback('False'))
        self.button_false.grid(row=2, column=1,padx=10, pady=10)
        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.label.config(text = f"Score: {self.quiz.score}")
            self.canvas.itemconfig(self.question_text,text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="End of the quiz")
            self.button_false.config(state="disabled")
            self.button_true.config(state="disabled")


    def give_feedback(self,user_answer):
        check = self.quiz.check_answer(user_answer)
        color = 'white'
        if check:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        self.window.after(1000,self.get_next_question)




