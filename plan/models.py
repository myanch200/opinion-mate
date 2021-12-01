from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Plan(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    
class Image(models.Model):
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/plan/')
    is_thumbnail = models.BooleanField(default=False)