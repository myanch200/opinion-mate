from django.http.response import JsonResponse
from django.shortcuts import render
from .models import Survey , Question , Option
from django.core import serializers

# Create your views here.
def get_questions(request, survey_id):
    survey = Survey.objects.get(id=survey_id)
    questions  = Question.objects.filter(survey=survey)
    data = []
    for question in questions:
        options = Option.objects.filter(question=question)
        options_data = []
        for option in options:
            option_temp = {
                "id": option.id,
                "text": option.text,
            }
            options_data.append(option_temp)
        temp = {
            "question_id": question.id,
            "question": question.text,
            'question_type': question.type,
            'points_worth': question.points_worth,
            'options': options_data,
        }
        data.append(temp)
    return JsonResponse(data, safe=False)


def survey(request, survey_id):
    survey = Survey.objects.get(id=survey_id)
    return render(request, 'survey/survey.html', {'survey': survey})