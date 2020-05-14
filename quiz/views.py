from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Question, Answer
from .serializers import QuestionSerializer, AnswerSerializer


@csrf_exempt
def question_list(request):
    if request.method == "GET":
        questions = Question.objects.all()
        serializer = QuestionSerializer(questions, many=True)
        return JsonResponse(serializer.data, safe=False)
    return


@csrf_exempt
def question_detail(request, pk):
    try:
        question = Question.objects.get(pk=pk)
    except:
        return HttpResponse(status=404)
    
    if request.method == "GET":
        serializer = QuestionSerializer(question)
        return JsonResponse(serializer.data)
    return

@csrf_exempt
def answer_list(request):
    if request.method == "GET":
        answers = Answer.objects.all()
        serializer = AnswerSerializer(answers, many=True)
        return JsonResponse(serializer.data, safe=False)
    return

@csrf_exempt
def answer_detail(request, pk):
    try:
        answer = Answer.objects.get(pk=pk)
    except:
        return HttpResponse(status=404)
    
    if request.method == "GET":
        serializer = AnswerSerializer(answer)
        return JsonResponse(serializer.data)
    return