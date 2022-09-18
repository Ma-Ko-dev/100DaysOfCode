class QuizBrain:

    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.user_score = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {question.text} (True/False) ")
        self.check_answer(user_answer, question.answer)

    def check_answer(self, user_answer, q_answer):
        if user_answer.lower() == q_answer.lower():
            print("You got it right!")
            self.user_score += 1
        else:
            print("That's wrong")
        print(f"The correct answer was {q_answer}")
        print(f"Your current score is: {self.user_score}/{self.question_number}\n")
