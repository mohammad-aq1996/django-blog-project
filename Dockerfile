FROM python:3.9.6-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SUPERUSER_PASSWORD admin

WORKDIR /usr/src/app

COPY ./requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD python manage.py makemigrations --noinput && \
    python manage.py migrate  --noinput && \
#    python manage.py collectstatic --noinput && \
    python manage.py createsuperuser --user admin --email admin@example.com --noinput ; \
    gunicorn -b 0.0.0.0:8000 mysite.wsgi:application