from django.http.response import JsonResponse
from django.shortcuts import render
from .forms import CommentForm
from plan.models import Plan
# Create your views here.
def add_comment(request, plan_id):
    plan = Plan.objects.get(id=plan_id)
    form = CommentForm(instance=plan)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.plan = plan
            comment.save()
            comment_serialized = {
                "comment_id": comment.id,
                "comment": comment.body,
                "created_at": comment.created_at,
                'author': comment.author.username,
            }
            return JsonResponse({'status':'success',"data":comment_serialized  }, status=200)
        else:
            return JsonResponse({'status':'error', 'message':"Comment creation failed"}, status=400)
    