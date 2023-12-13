from django.db import models
from django.utils.timezone import now
# Create your models here.

class Question(models.Model):
    set = models.ForeignKey("Set", on_delete=models.CASCADE)
    question = models.CharField(max_length=255)

    answer_a = models.CharField(max_length=255)
    answer_a_file = models.ImageField(upload_to="image_option", null=True)

    answer_b = models.CharField(max_length=255)
    answer_b_file = models.ImageField(upload_to="image_option", null=True)

    answer_c = models.CharField(max_length=255)
    answer_c_file = models.ImageField(upload_to="image_option", null=True)

    answer_d = models.CharField(max_length=255)
    answer_d_file = models.ImageField(upload_to="image_option", null=True)

    correct_answer = models.CharField( max_length=255)

    def __repr__(self) -> str:
        return self.question


class Set(models.Model):
    posted_datetime = models.DateTimeField(default=now())
    title = models.CharField(null=True, max_length=255)
    file = models.ImageField(upload_to="csv_files")

    def __repr__(self) -> str:
        return self.title