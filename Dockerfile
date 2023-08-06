FROM python:3.10.6

WORKDIR /app

COPY . /app/

RUN pip install -r requirements.txt

ENV PORT=8000

RUN python manage.py collectstatic --noinput | python manage.py migrate

EXPOSE 8000

#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
CMD [
"gunicorn",  "oc_lettings_site.wsgi:application", "--bind", "0.0.0.0:$PORT"
]