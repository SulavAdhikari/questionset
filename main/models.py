from django.db import models
from django.utils.timezone import datetime
# Create your models here.

class Question(models.Model):
    set = models.ForeignKey("Set", on_delete=models.CASCADE)
    question = models.CharField()
    
    answer_a = models.CharField()
    answer_b = models.CharField()
    answer_c = models.CharField()
    answer_d = models.CharField()

    CHOICES = [
        ('A', 'Option A'),
        ('B', 'Option B'),
        ('C', 'Option C'),
        ('D', 'Option D'),
    ]

    correct_answer = models.CharField(choices=CHOICES)


class Set(models.Model):
    posted_datetime = models.DateTimeField(default=datetime.now())
    title = models.CharField(null=True)