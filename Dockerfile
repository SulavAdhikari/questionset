
FROM python:3.11.4


WORKDIR /usr/src/app

COPY . .


RUN pip install --no-cache-dir -r requirements.txt


EXPOSE 8000

# Define environment variable
ENV DJANGO_SETTINGS_MODULE=questionset.settings


CMD ["gunicorn", "questionset.wsgi:application", "--bind", "0.0.0.0:8000"]
