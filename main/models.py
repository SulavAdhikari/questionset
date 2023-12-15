from django.db import models
from django.utils.timezone import now
from django.core.files.base import ContentFile
from PIL import Image
from io import BytesIO
# Create your models here.

class Question(models.Model):
    set = models.ForeignKey("Set", on_delete=models.CASCADE)
    question = models.CharField(max_length=255)

    answer_a = models.CharField(max_length=255, null=True)
    answer_a_file = models.ImageField(upload_to="image_option", null=True)

    answer_b = models.CharField(max_length=255, null=True)
    answer_b_file = models.ImageField(upload_to="image_option", null=True)

    answer_c = models.CharField(max_length=255, null=True)
    answer_c_file = models.ImageField(upload_to="image_option", null=True)

    answer_d = models.CharField(max_length=255, null=True)
    answer_d_file = models.ImageField(upload_to="image_option", null=True)

    correct_answer = models.CharField( max_length=255)

    def __repr__(self) -> str:
        return self.question

    def save(self, *args, **kwargs):
        for field_name in ['answer_a_file', 'answer_b_file', 'answer_c_file', 'answer_d_file']:
            image_field = getattr(self, field_name)
            
            # Check if the field is a BytesIO object
            if isinstance(image_field, BytesIO):
                # Create a PIL Image object from the BytesIO
                image = Image.open(image_field)

                # Create a BytesIO buffer to save the image
                image_buffer = BytesIO()

                # Save the image to the buffer in JPEG format
                image.save(image_buffer, format='JPEG')

                # Create a ContentFile from the buffer
                image_content = ContentFile(image_buffer.getvalue(), name=f'{field_name}_default.jpg')

                # Assign the ContentFile to the ImageField
                setattr(self, field_name, image_content)

        super(Question, self).save(*args, **kwargs)

class Set(models.Model):
    posted_datetime = models.DateTimeField(default=now())
    title = models.CharField(null=True, max_length=255)
    file = models.ImageField(upload_to="csv_files")

    def __repr__(self) -> str:
        return self.title