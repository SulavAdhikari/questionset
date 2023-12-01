import pandas as pd
from django.shortcuts import render, redirect
from .forms import QuestionSetUploadForm 
from .models import Question, Set  
import io, os
from django.views.decorators.csrf import csrf_protect
from questionset.settings import MEDIA_ROOT

@csrf_protect
def upload_question_set(request):
    if request.method == 'POST':
        form = QuestionSetUploadForm(request.POST, request.FILES)
        if form.is_valid():
            
            ins = form.save(commit=True)
            file = ins.file
            if file.name.endswith('.csv'):
                # df = pd.read_csv(file)
                string = file.read()
                df = pd.read_csv(os.path.join(MEDIA_ROOT ,file.name), index_col=None)
            else:  
                df = pd.read_excel(os.path.join(MEDIA_ROOT ,file.name))
            print(df)
            # Iterate through the DataFrame and save each row to the database
            for index, row in df.iterrows():
                Question.objects.create(
                    set=ins,
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
