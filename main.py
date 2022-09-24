from data import question_data
from question_model import Question
from quiz_brain import QuizBrain
Question_Bank =[]
for question in question_data:
    question_text = question['text']
    question_answer = question['answer']
    new_question =Question(question_text,question_answer)
    Question_Bank.append(new_question)
quiz =QuizBrain(Question_Bank)
while quiz.still_have_question():
    quiz.next_question()
print("You have completed the quiz.")
print(f"Your current score was : {quiz.score}/{quiz.question_number}.")