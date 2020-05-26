from django.db import models

class Question(models.Model):
    question = models.CharField("Question", max_length=400)

    def __str__(self):
        return self.question
    
    def has_correct_answer(self, pk):
        return len(Answer.objects.filter(question__id=pk, correct=True)) > 0

    def correct_answer(self, pk):
        return Answer.objects.filter(question__id=pk, correct=True)

    def start_quiz(self, questions_number):
        questions = Question.objects.filter()
        if questions_number > len(questions):
            questions_number = len(questions)
        questions = questions.order_by('?')[:questions_number]
        return questions


class Answer(models.Model):
    answer = models.CharField("Answer", max_length=255)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="answers")
    correct = models.BooleanField("Correct Answer")

    def __str__(self):
        return self.answer

    def save(self, *args, **kwargs):
        if self.correct == True:
            if Question().has_correct_answer(self.question.pk):
                return "Question already has a correct answer."
        super(Answer, self).save(*args, **kwargs)

    def get(self, pk):
        try:
            return Answer.objects.get(pk=pk)
        except:
            return "Answer not found."


class QuizUser(models.Model):
    name = models.CharField("Name", max_length=50)
    has_answered = models.BooleanField("Has answered", default=False)
    questions_answered = models.IntegerField("Questions Answered")
    right_questions = models.IntegerField("Right Questions")

    def __str__(self):
        return self.name

    def user_exists(self, pk):
        return len(QuizUser.objects.filter(pk=pk)) > 0