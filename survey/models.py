from django.db import models
from django.contrib.auth.models import User
from plan.models import Plan
# Create your models here.
class Servey(models.Model):
    plan = models.OneToOneField(Plan, on_delete=models.CASCADE)
    points = models.IntegerField(default=0)
    patricipants = models.ManyToManyField(User, related_name='participants')
    def __str__(self):
        return f"Servey- {self.plan.title}"
    
class Question(models.Model):
    TYPE = (('Normal','Normal'), ('Open Answer', 'Open Answer'))
    text = models.CharField(max_length=200)
    survey = models.ForeignKey(Servey, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    points_worth = models.IntegerField(default=0)
    type = models.CharField(max_length=50, choices=TYPE, default='Normal')
    def __str__(self):
        return self.text
    

class Option(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    class Meta:
        abstract = True

class OpenOption(Option):
    text = models.TextField()
    
    def __str__(self):
        return self.text

class ShortOption(Option):
    text = models.CharField(max_length=200)
    
    def __str__(self):
        return self.text
