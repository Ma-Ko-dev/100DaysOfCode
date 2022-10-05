from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ("Arial", 18, "italic")
TRUE_IMG = "images/true.png"
FALSE_IMG = "images/false.png"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # Label
        self.label_score = Label(text="Score: 0", bg=THEME_COLOR, fg="white")
        self.label_score.grid(row=0, column=1)

        # Canvas
        self.canvas_q = Canvas(self.window, bg="white", width=300, height=250)
        self.canvas_q_text = self.canvas_q.create_text(150, 125, text="Question here", font=FONT, fill=THEME_COLOR,
                                                       width=280)
        self.canvas_q.grid(row=1, column=0, columnspan=2, pady=50)

        # Buttons
        self.btn_true_img = PhotoImage(file=TRUE_IMG)
        self.btn_true = Button(self.window, image=self.btn_true_img, highlightthickness=0, command=self.send_true)
        self.btn_true.grid(row=2, column=0)

        self.btn_false_img = PhotoImage(file=FALSE_IMG)
        self.btn_false = Button(self.window, image=self.btn_false_img, highlightthickness=0, command=self.send_false)
        self.btn_false.grid(row=2, column=1)

        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas_q.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.label_score.config(text=f"Score: {self.quiz.score}")
            self.canvas_q.itemconfig(self.canvas_q_text, text=q_text)
        else:
            self.canvas_q.itemconfig(self.canvas_q_text, text="You have reached the end of the quiz.")
            self.btn_true.config(state="disabled")
            self.btn_false.config(state="disabled")

    def send_true(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def send_false(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas_q.config(bg="green")
        else:
            self.canvas_q.config(bg="red")
        self.window.after(1000, self.get_next_question)

