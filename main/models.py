from django.db import models
from django.utils.timezone import now
# Create your models here.

class Question(models.Model):
    set = models.ForeignKey("Set", on_delete=models.CASCADE)
    question = models.CharField(max_length=255)
    
    answer_a = models.CharField(max_length=255)
    answer_b = models.CharField(max_length=255)
    answer_c = models.CharField(max_length=255)
    answer_d = models.CharField(max_length=255)



    correct_answer = models.CharField( max_length=255)


class Set(models.Model):
    posted_datetime = models.DateTimeField(default=now())
    title = models.CharField(null=True, max_length=255)
    file = models.ImageField(upload_to="csv_files")