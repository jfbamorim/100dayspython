class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def retrieve_question(self):
        actual_question = self.question_list[self.question_number]
        self.question_number += 1
        answer = input(f"Q.{self.question_number} {actual_question.text} (True/False)?: ")
        self.check_answer(answer, actual_question.answer)

    def check_answer(self, user_ans, quest_ans):
        if user_ans.lower() == quest_ans.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("You got it wrong.")
        print(f"The current answer was {quest_ans}.")
        print(f"Your current score is {self.score}/{self.question_number}\n")


