from tkinter import *
from quiz_brain import QuizBrain
MY_FONT = ("Arial", 20, "italic")
THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.score = 0
        self.window = Tk()
        self.window.title("Quizzler Quiz App. ❔❔")
        self.window.config(bg=THEME_COLOR, pady=20, padx=20)

        self.label = Label(text=f"Score :{self.score}")
        self.label.config(bg=THEME_COLOR, fg="white")
        self.label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, highlightbackground=THEME_COLOR)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        self.q_txt = self.canvas.create_text(150, 125, width=280, text="Some Text", font=MY_FONT)

        r_image = PhotoImage(file="images/true.png")
        self.btn_r = Button(image=r_image, command=self.true_answer)
        self.btn_r.grid(row=2, column=0)

        l_image = PhotoImage(file="images/false.png")
        self.btn_l = Button(image=l_image, command=self.false_answer)
        self.btn_l.grid(row=2, column=1)

        self.add_next_question()
        self.window.mainloop()

    def add_next_question(self):
        if self.quiz.still_has_questions():
            self.canvas.config(bg="white")
            que_txt = self.quiz.next_question()
            self.canvas.itemconfig(self.q_txt, text=que_txt)
        else:
            self.canvas.config(bg="white")
            self.canvas.itemconfig(self.q_txt, text=f"You've reached the end of the "
                                                    f"quiz Your Final Score : {self.score}")
            self.btn_r.config(state="disabled")
            self.btn_l.config(state="disabled")

    def increase_score(self):
        self.score += 1
        self.label.config(text=f"Score : {self.score}")

    def true_answer(self):
        if self.quiz.check_answer("True"):
            self.canvas.config(background="green")
            self.increase_score()
        else:
            self.canvas.config(background="red")
        self.window.after(1000, self.add_next_question)

    def false_answer(self):
        if self.quiz.check_answer("False"):
            self.canvas.config(background="green")
            self.increase_score()
        else:
            self.canvas.config(background="red")
        self.window.after(1000, self.add_next_question)
