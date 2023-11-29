from django.shortcuts import render, redirect
from .forms import QuestionSetUploadForm
from .models import Question, Set
import csv
import io

def upload_question_set(request):
    if request.method == 'POST':
        form = QuestionSetUploadForm(request.POST, request.FILES)
        if form.is_valid():
            question_set = Set.objects.create(title="Uploaded Set")
            file = request.FILES['file']
            decoded_file = file.read().decode('utf-8')
            io_string = io.StringIO(decoded_file)
            reader = csv.reader(io_string)
            for row in reader:
                Question.objects.create(
                    set=question_set,
                    question=row[0],
                    answer_a=row[1],
                    answer_b=row[2],
                    answer_c=row[3],
                    answer_d=row[4],
                    correct_answer=row[5]
                )
            return redirect('upload_success')
    else:
        form = QuestionSetUploadForm()
    return render(request, 'upload.html', {'form': form})

def upload_success(request):
    return render(request, 'upload_success.html')
