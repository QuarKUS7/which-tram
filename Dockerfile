FROM python:3.6-alpine
WORKDIR /app

RUN apk --update add --no-cache g++ udev chromium chromium-chromedriver

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD python app.py
