FROM python:3.12

WORKDIR /usr/app

RUN apt-get update && apt-get install firefox-esr -y

COPY requirements.txt  .

RUN pip install -r requirements.txt

RUN mkdir prices

COPY . .

CMD [ "python", "main.py"]