from django.db import models

class Question(models.Model):
    question = models.CharField("Question", max_length=400)

    def __str__(self):
        return self.question


class Answer(models.Model):
    answer = models.CharField("Answer", max_length=255)
    question = models.ForeignKey("Question", name="Question", on_delete=models.CASCADE, related_name="answers")
    correct = models.BooleanField("Correct Answer")

    def __str__(self):
        return self.answer
    
