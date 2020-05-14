from django.urls import path
from .views import question_detail, question_list, answer_list, answer_detail

urlpatterns = [
    path("questions/", question_list),
    path("questions/<int:pk>", question_detail),
    path("answers/", answer_list),
    path("answers/<int:pk>", answer_detail),
]
