from django.forms import ModelForm , Textarea
from .models import Comment
class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['body']
        widgets = {
            'body': Textarea(attrs={'cols': 50, 'rows': 3}),
        }
        