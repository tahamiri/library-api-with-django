FROM python:3.10-slim

WORKDIR /src

COPY requirements.txt /src/

RUN pip install -U pip

RUN pip install -r requirements.txt

COPY . /src/

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]