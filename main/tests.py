from django.test import TestCase, Client
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
from .models import Question, Set
import os

class QuestionSetUploadTests(TestCase):

    def setUp(self):
        # Set up the client and other necessary setups
        self.client = Client()
        self.upload_url = reverse('question_set_upload')

    def test_upload_valid_csv_file(self):
        # Test uploading a valid CSV file
        with open('testfiles/test.csv', 'rb') as file:
            response = self.client.post(self.upload_url, {'file': file}, format='multipart')
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Set.objects.count(), 1)
        self.assertEqual(Question.objects.count(), 3)

    def test_upload_valid_excel_file(self):
        # Test uploading a valid Excel file
        with open('testfiles/test_e.xlsx', 'rb') as file:
            response = self.client.post(self.upload_url, {'file': file}, format='multipart')
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Set.objects.count(), 1)
        self.assertEqual(Question.objects.count(), 2)

    def test_upload_invalid_file_type(self):
        # Test uploading an invalid file type
        invalid_file = SimpleUploadedFile("file.txt", b"file_content", content_type="text/plain")
        response = self.client.post(self.upload_url, {'file': invalid_file})

        self.assertIn('The file must be a CSV or Excel file.', response.content.decode())

    def test_upload_file_with_wrong_columns(self):
        # Test uploading a file with the wrong number of columns
        with open('testfiles/wrongcoltest.csv', 'rb') as file:
            response = self.client.post(self.upload_url, {'file': file}, format='multipart')
        self.assertIn('The file must have exactly 6 columns.', response.content.decode())

    def test_question_model(self):
        # Test creating a question
        set_instance = Set.objects.create(title="Test Set")
        Question.objects.create(set=set_instance, question="Test Question", answer_a="A", answer_b="B", answer_c="C", answer_d="D", correct_answer="A")

        self.assertEqual(Question.objects.count(), 1)
        question = Question.objects.first()
        self.assertEqual(question.question, "Test Question")
        self.assertEqual(question.correct_answer, "A")

    # You can add more tests as needed

