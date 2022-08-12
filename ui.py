from tkinter import *
from quiz_brain import QuizBrain
from question_model import Question


THEME_COLOR = "#375362"

class UI:
    
    
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.root = Tk()
        self.root.title("Quizzler")
        self.root.config(background=THEME_COLOR, padx=20, pady=20)
        
        true_image = PhotoImage(file='images/true.png')
        false_image = PhotoImage(file='images/false.png')
        
        self.score_label = Label(text="Score: 0", bg=THEME_COLOR, fg='white')
        self.score_label.grid(column=1, row=0, padx=20, pady=20)

        self.question_canv = Canvas(self.root, width=300, height=250, highlightthickness=0)
        self.question_text = self.question_canv.create_text(150, 125, width=260, fill=THEME_COLOR, font=('Arial', 20, 'italic'))
        self.question_canv.grid(column=0, row=1, columnspan=2, padx=20, pady=20)

        self.true_button = Button(image=true_image, highlightbackground=THEME_COLOR,command=self.is_true)
        self.true_button.grid(column=0, row=3, padx=20, pady=20)

        self.false_button = Button(image=false_image, highlightbackground=THEME_COLOR, command=self.is_false)
        self.false_button.grid(column=1, row=3, padx=20, pady=20)
        
        self.get_next_question()
        
        
        self.root.mainloop()


    def get_next_question(self):
        self.question_canv.config(background='white')
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.score_label.config(text=f"Score: {self.quiz.score}", bg=THEME_COLOR, fg='white')
            self.question_canv.itemconfig(self.question_text, text=q_text)
        else:
            self.true_button.config(state='disabled')
            self.false_button.config(state='disabled')
            self.question_canv.itemconfig(self.question_text, text=f"Your final score is: {self.quiz.score}/10")


    def is_true(self):
        is_right = self.quiz.check_answer('True')
        self.give_feedback(is_right)
    
    
    def is_false(self):
        is_right = self.quiz.check_answer('False')
        self.give_feedback(is_right)
            
    
    def give_feedback(self, is_right):
        if is_right == True:
            self.question_canv.config(background='green')
            self.root.after(400, self.get_next_question)
        else:
            self.question_canv.config(background='red')
            self.root.after(400, self.get_next_question)





    