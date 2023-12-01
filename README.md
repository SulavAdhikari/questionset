# Django Question Set Upload Web App

## Overview

This Django web application facilitates the uploading of question sets, primarily handling CSV and XLSX files. It features a simple upload form designed with Tailwind CSS and is dockerized for convenient deployment and usage.

## Features

- **Upload Form:** Located at `/questionset/upload` for easy file submissions.
- **File Format Support:** Accepts only CSV and XLSX files.
- **Required Columns:** Files must include the following columns: `question`, `answer_a`, `answer_b`, `answer_c`, `answer_d`, `correct_answer`.
- **Data Validation:** Ensures files adhere to the required format before saving to the database.
- **File Storage:** Uploaded files are stored on the server.
- **Tailwind CSS:** Provides a user-friendly and responsive interface.
- **Docker Integration:** The application is containerized for consistent deployment across different environments.

## Installation

```
git clone <repo>
cd questionset
sudo docker-compose up --build
```

## Usage

1. **Access the Upload Form:** 
   Navigate to `http://localhost/questionset/upload` in your web browser.

2. **Uploading a File:** 
   Use the form to upload your CSV or XLSX file.

3. **Validation and Storage:** 
   The app validates the file and stores it in the database and server if it meets the format requirements.

## Running Tests

The application includes tests covering its basic functionalities. To execute these tests, use the designated command in your development setup.
```
python manage.py test
```


