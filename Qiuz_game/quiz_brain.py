class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.score = 0
        self.question_list = question_list

    def still_has_question(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        ans = input(f"Q.{self.question_number +
                    1}: {current_question.text}.(True/False)?:")
        self.check_answer(ans, current_question.answer)
        self.question_number += 1

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("Correct answer")
            self.score += 1
        else:
            print("Wrong answer")

        print(f"The correct answer was {correct_answer}.")
        print(f"Your current score is:{self.score}/{self.question_number+1}")
        print("\n")
