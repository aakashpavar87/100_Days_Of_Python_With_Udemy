class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list

    def check_answer(self, player_answer, current_answer, q_no):
        if player_answer.lower() == current_answer.lower():
            print("Yeh You Answered Correctly 🤩")
            self.question_number += 1
            print(f"You are One Question {q_no + 1}/{q_no + 1}")
            self.next_question()
        else:
            print("Oh You get It Wrong !!!!")
            print(f"Correct Answer is : {current_answer}")
            print(f"You are One Question {q_no}/{q_no + 1}")
            return

    def next_question(self):
        q_no = self.question_number
        question_txt = self.question_list[q_no].question
        q_answer = self.question_list[q_no].correct_answer
        player_answer = input(f"Q.{q_no + 1} {question_txt} (True/False): ")
        self.check_answer(player_answer, q_answer, q_no)
