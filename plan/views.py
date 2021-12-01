from django.shortcuts import get_object_or_404, render
from .models import Plan , Image
from comment.forms import CommentForm
# Create your views here.
def detailed_plan(request, plan_id):
    form = CommentForm()
    plan = get_object_or_404(Plan, pk=plan_id)
    images = Image.objects.filter(plan=plan)
    context ={
            'plan': plan,
            'images' : images,
            'form': form}
    return render(request, 'plan/detailed_plan.html', context)