from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.upload_question_set, name='upload_question_set'),
    path('upload/success/', views.upload_success, name='upload_success'),
]