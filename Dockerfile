FROM python:3.9

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY ./student_management_system /code/student_management_system

EXPOSE 8000

CMD ["python", "student_management_system/manage.py", "runserver", "127.0.0.1:8000"]
