from question_model import QuestionModel
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    # question_obj = QuestionModel(question["text"], question["answer"])
    question_obj = QuestionModel(question["question"], question["correct_answer"])
    question_bank.append(question_obj)
my_quiz_brain = QuizBrain(question_bank)
my_quiz_brain.next_question()
