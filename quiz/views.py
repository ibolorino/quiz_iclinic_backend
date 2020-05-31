from rest_framework.response import Response
from .models import Question, Answer, QuizUser
from .serializers import QuestionSerializer, AnswerSerializer
from .utils import check_user, count_correct_answers
from rest_framework import generics
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser


class QuestionList(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class QuestionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class AnswerList(generics.ListCreateAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer

class AnswerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer


@api_view(['POST'])
def start_quizz(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        questions_number = data['questions_number']
        questions = Question().start_quiz(questions_number)
        serializer = QuestionSerializer(questions, many=True)
        return Response(serializer.data)

@api_view(['POST'])
def login(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        username = data['username']
        user = check_user(username)
        return Response(user)


@api_view(['POST'])
def submit_quizz(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        total = len(data['result'])
        correct = count_correct_answers(data['result'])
        user = QuizUser.objects.filter(name=data['username'])
        user.update(has_answered=True, questions_answered=total, right_questions=correct)
        result = {
            'correct': correct,
            'total': total,
        }

        return Response(result)