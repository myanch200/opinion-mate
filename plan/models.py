from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Plan(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title
    
    def get_thumbnail(self):
        return self.images.first().image.url
class Image(models.Model):
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='images/plan/')
    is_thumbnail = models.BooleanField(default=False)