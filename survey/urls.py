from django.urls import path
from .views import get_questions, survey
app_name = 'survey'

urlpatterns = [
    path('survey/<int:survey_id>/',survey,name='survey'),
    path('get-questions/<int:survey_id>', get_questions, name='get_questions'),
]
