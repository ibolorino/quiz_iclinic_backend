from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from quiz import views
from .views import *

urlpatterns = [
    path("questions/", views.QuestionList.as_view()),
    path("questions/<int:pk>", views.QuestionDetail.as_view()),
    path("answers/", views.AnswerList.as_view()),
    path("answers/<int:pk>", views.AnswerDetail.as_view()),
    path("start_quizz", start_quizz),
    path("login", login),
]

urlpatterns = format_suffix_patterns(urlpatterns)