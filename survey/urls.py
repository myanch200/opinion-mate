from django.urls import path
from .views import get_questions, take_survey
app_name = 'survey'

urlpatterns = [
    path('survey/<int:survey_id>/',take_survey,name='take_survey'),
    path('get-questions/<int:survey_id>', get_questions, name='get_questions'),
]
