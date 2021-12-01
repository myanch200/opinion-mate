from django.http.response import JsonResponse
from django.shortcuts import render
from .forms import CommentForm
from plan.models import Plan
# Create your views here.
def add_comment(request, plan_id):
    plan = Plan.objects.get(id=plan_id)
    form = CommentForm(instance=plan,author=request.user)
    if request.method == 'POST':
        form = CommentForm(instance=plan, data=request.POST)
        if form.is_valid():
            comment = form.save()
            return JsonResponse({'status':'success'}, status=200)
        else:
            return JsonResponse({'status':'error'}, status=400)
    