FROM python:3.10.6

WORKDIR /app

COPY . /app/

RUN pip install -r requirements.txt

EXPOSE 8000

#CMD ["python", "manage.py", "runserver", "127.0.0.1:8000"]
#CMD ["python", "manage.py", "runserver", "localhost:8000"]
CMD ["python", "manage.py", "runserver"]
