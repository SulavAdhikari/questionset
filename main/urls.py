from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.upload_question_set, name='question_set_upload'),
]