FROM python:3.8.10

WORKDIR /app

COPY requirements.txt requirements.txt

RUN apt-get clean && apt-get update
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .

CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0", "--port=5000"]

EXPOSE 5000