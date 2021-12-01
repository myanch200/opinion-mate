from django.urls import path
from .views import detailed_plan
app_name = "plan"

urlpatterns = [
    path('plan/<int:plan_id>/', detailed_plan, name='detailed_plan'),
]