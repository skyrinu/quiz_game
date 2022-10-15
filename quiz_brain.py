class QuizBrain:
    def __init__(self, question_list):
        self.right_or_wrong = None
        self.user_answer = None
        self.current_question = None
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def next_question(self):
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        self.user_answer = input(f"Q.{self.question_number} {self.current_question.text} (True or False): ").lower()

    def questions_left(self):
        return self.question_number < len(self.question_list)

    def evaluate(self):
        if self.user_answer == self.current_question.answer.lower():
            self.score += 1
            self.right_or_wrong = "right"
        else:
            self.right_or_wrong = "wrong"

    def result(self):
        print(f"You got it {self.right_or_wrong}.")
        print(f"The correct answer was: {self.current_question.answer}")
        print(f"Your current score is {self.score}/{self.question_number}")
        print("")

    def final_result(self):
        print("You've completed the quiz")
        print(f"Your final score was {self.score}/{self.question_number}")
