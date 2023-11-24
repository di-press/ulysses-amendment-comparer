FROM python:3.8.7

WORKDIR /app

COPY requirements.txt requirements.txt
RUN apt-get clean
RUN apt-get update --allow-unauthenticated --allow-insecure-repositories
RUN apt-get -y install libpq-dev gcc
RUN pip install --upgrade pip
RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python3", "app.py"]
EXPOSE 5000