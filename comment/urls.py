from django.urls import path
from .views import add_comment
app_name = 'comment'

urlpatterns = [
    path('add_comment/<int:plan_id>/', add_comment, name='add_comment'),
]
