import pandas as pd
from django.shortcuts import render, redirect
from .forms import QuestionSetUploadForm 
from .models import Question, Set  
import os, openpyxl
from PIL import Image
from django.views.decorators.csrf import csrf_protect
from questionset.settings import MEDIA_ROOT
from django.contrib import messages


@csrf_protect
def upload_question_set(request):
    if request.method == 'POST':
        form = QuestionSetUploadForm(request.POST, request.FILES)
        if form.is_valid():
            
            ins = form.save(commit=True)
            file = ins.file
            if file.name.endswith('.csv'):
                
                df = pd.read_csv(os.path.join(MEDIA_ROOT ,file.name), index_col=None)
            else:
                df = pd.read_excel(os.path.join(MEDIA_ROOT ,file.name))
                from .scripts import ExcelHelper
                
                work_book = openpyxl.load_workbook(os.path.join(MEDIA_ROOT ,file.name))
                sheet = work_book.active
                excel_client = ExcelHelper(sheet=sheet)

                if excel_client.has_image:
                    rows = excel_client.get_all_rows()

                    for index, row in df.iterrows():

                        if index not in rows:
                            Question.objects.create(
                            set=ins,
                            question=row[0],
                            answer_a=row[1],
                            answer_b=row[2],
                            answer_c=row[3],
                            answer_d=row[4],
                            correct_answer=row[5]
                            )
                        else:
                            options = excel_client.get_cols_by_row(index)
                            q = Question(set=ins, question=row[0])
                            if "A" in options:
                                image = excel_client.locate_image(index, 'A')
                                q.answer_a_file = image
                                
                            else:
                                q.answer_a= row[1]

                            if "B" in options:
                                image = excel_client.locate_image(index, 'B')
                                q.answer_b_file = image
                            else:
                                q.answer_b = row[2]

                            if "C" in options:
                                image = excel_client.locate_image(index, 'c')
                                q.answer_c_file = image
                            else:
                                q.answer_c = row[3]

                            if "D" in options:
                                image = excel_client.locate_image(index, 'D')
                                q.answer_d_file = image
                            else:
                                q.answer_d = row[4]
                            q.correct_answer=row[5]
                            q.save()
                    messages.success(request, "Upload Sucess with images")
                    return render(request, 'upload.html', {'form':form})
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
            
            messages.success(request, "Upload Sucessful." )

    else:
        form = QuestionSetUploadForm()
    return render(request, 'upload.html', {'form': form})

