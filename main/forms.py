from django import forms
import csv, io, openpyxl

class QuestionSetUploadForm(forms.Form):
    file = forms.FileField()

    def clean_file(self):
        uploaded_file = self.cleaned_data['file']
        file_name = uploaded_file.name
        if not (file_name.endswith('.csv') or file_name.endswith('.xlsx')):
            raise forms.ValidationError("The file must be a CSV or Excel file.")

        # Check if the file is in the correct format
        try:
            if file_name.endswith('.csv'):
                decoded_file = uploaded_file.read().decode('utf-8')
                io_string = io.StringIO(decoded_file)
                reader = csv.reader(io_string)
                for row in reader:
                    if len(row) != 6:
                        raise forms.ValidationError("CSV file format is incorrect.")
            else:  # Excel file
                wb = openpyxl.load_workbook(filename=uploaded_file)
                sheet = wb.active
                for row in sheet.iter_rows():
                    if len(row) != 6:
                        raise forms.ValidationError("Excel file format is incorrect.")
        except Exception as e:
            raise forms.ValidationError(f"Error reading file: {str(e)}")

        # Return the cleaned data.
        return uploaded_file
