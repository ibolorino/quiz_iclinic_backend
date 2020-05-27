from .models import *

def its_correct_answer(answer_id, question_id):
    answer = Answer().get(answer_id)
    if answer.correct == True:
        if answer.question.id == question_id:
            return True
    return False

def count_correct_answers(quiz):
    correct_answers = 0
    for question in quiz['quiz']:
        if its_correct_answer(question['answer'], question['question']):
            correct_answers += 1
    return correct_answers

def check_user(username):
    user = QuizUser().user_exists(username)
    if not user:
        QuizUser(name=username).save()
        user = QuizUser().user_exists(username)
    return user
