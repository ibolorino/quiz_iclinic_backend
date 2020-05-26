from rest_framework.response import Response
from .models import Question, Answer
from .serializers import QuestionSerializer, AnswerSerializer
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

@csrf_exempt
@api_view(['GET'])
def start_quiz(request):
    if request.method == 'GET':
        data = JSONParser().parse(request)
        questions_number = data['questions_number']
        username = data['username']
        questions = Question().start_quiz(questions_number)
        serializer = QuestionSerializer(questions, many=True)
        if questions_number < 1:
            return Response("error")
        return Response(serializer.data)

