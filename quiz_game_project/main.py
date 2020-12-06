from quiz_game_project.quiz_game_data import question_data
from quiz_game_project.Question import Question
from quiz_game_project.quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    q_text = question["question"]
    q_answer = question["correct_answer"]
    newQuestion = Question(q_text, q_answer)
    question_bank.append(newQuestion)

quiz_brain = QuizBrain(question_bank)

while quiz_brain.still_has_questions():
    quiz_brain.retrieve_question()
print("You've completed the quiz.")
print(f"Your final score was {quiz_brain.score}/{quiz_brain.question_number}")
