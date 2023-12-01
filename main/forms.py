from django import forms
import pandas as pd
from .models import Question, Set


class QuestionSetUploadForm(forms.Form):
    file = forms.FileField()

    def clean_file(self):
        file = self.cleaned_data['file']

        # Validate file type
        if not (file.name.endswith('.csv') or file.name.endswith('.xlsx')):
            raise forms.ValidationError('The file must be a CSV or Excel file.')

        # Read file and validate columns
        if file.name.endswith('.csv'):
            df = pd.read_csv(file)
        else:  # Excel file
            df = pd.read_excel(file)

        if df.shape[1] != 6:
            raise forms.ValidationError('The file must have exactly 6 columns.')

        # Check for required column names
        # required_columns = ['question', 'answer_a', 'answer_b', 'answer_c', 'answer_d', 'correct_answer']
        # if not all(column in df.columns for column in required_columns):
        #     raise forms.ValidationError('The file must contain the required columns: question, option a, option b, option c, option d, correct answer.')

        return file
    

    def save(self, commit=True):
        
        file = self.cleaned_data['file']

        instance = Set(title = file.name, file=file)
        if commit:
            instance.save()
        return instance